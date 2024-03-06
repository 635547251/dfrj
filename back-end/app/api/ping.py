from flask import request, jsonify, url_for, g, current_app
from app.api import bp
from app.api.errors import bad_request, error_parameter, error_api
from util.common import dify_mbti
import json
from zhipuai import ZhipuAI

@bp.route('/ping', methods=['GET'])
def ping():
    '''前端用来测试与后端Flask API的连通性'''
    return jsonify('Pong!')

@bp.route('/zhipu_test', methods=['POST'])
def zhipu_test():
    '''测试智谱API'''
    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    question=data
    if 'role' not in question.keys():
        return error_parameter('role')
    if 'content' not in question.keys():
        return error_parameter('content')
    if 'model' not in question.keys():
        model=current_app.config['MODEL_ZHIPU']
    else:
        model=question['model']
    try:
        client = ZhipuAI(api_key=current_app.config['ZHIPU_API_KEY'])
        res = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": question['role'],
                    "content": question['content']
                }
            ],
        )
        message={
            'message':{
                'role':res.choices[0].message.role,
                'content':res.choices[0].message.content,
            },
            'request':{
                'request_id':res.request_id,
                'id':res.id,
            },
            'usage':{
                'prompt_tokens':res.usage.prompt_tokens,
                'completion_tokens':res.usage.completion_tokens,
                'total_tokens':res.usage.total_tokens,
            }
        }
        response = jsonify(message)
        return response
    except Exception as e:
        return error_api(e.args)

@bp.route('/dify_test', methods=['POST'])
def dify_test():
    '''测试Dify API'''
    data = request.get_json()
    # 参数检验
    if not data:
        return bad_request('You must post JSON data.')
    question=data
    if 'role' not in question.keys():
        return error_parameter('role')
    if 'content' not in question.keys():
        return error_parameter('content')
    if 'conversation_id' not in question.keys():
        conversation_id=''
    else:
        conversation_id=question['conversation_id']
    # 数据获取
    try:
        res=dify_mbti(
            query=question['content'],
            conversation_id=conversation_id, 
            user=question['role'],
            api_url=current_app.config['DIFY_URL'],
            api_key=current_app.config['DIFY_API_KEY']
        )
        if res.status_code == 200:
            message={
                "task_id": "191608a0-7a7c-43c9-8286-631f59e6e211", 
                "id": "92e32983-0e5f-421d-bd08-9cc7bc523d5c", 
                "message_id": "92e32983-0e5f-421d-bd08-9cc7bc523d5c", 
                "conversation_id": "8b81eacc-4d3d-4f7e-b761-a44edfee60ea", 
                'answer':'',
                "metadata": {}
            }
            def generate(res):
                for chunk in res.iter_lines():
                    if chunk:
                        data=json.loads(chunk.decode('utf-8').replace('data:',''))
                        if data['event']=='message':
                            message['answer']+=data['answer']
                            yield data['answer']
                        elif data['event']=='message_end':
                            message['task_id']=data['task_id']
                            message['id']=data['id']
                            message['message_id']=data['message_id']
                            message['conversation_id']=data['conversation_id']
                            message['metadata']=data['metadata']
                            print(message)
                            yield '\n'+message['answer']
            return generate(res)
        else:
            return error_api(res)
    except Exception as e:
        return error_api(e.args)
