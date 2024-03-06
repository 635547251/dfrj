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
            messages=[]
            def generate(res):
                for chunk in res.iter_lines():
                    if chunk:
                        data=json.loads(chunk.decode('utf-8').replace('data:',''))
                        if data['event']=='message':
                            messages.append(data)
                            yield data['answer']
                        elif data['event']=='message_end':
                            messages.append(data)
                            print(messages)
                            yield jsonify(data)
            return generate(res)
        else:
            return error_api(res)
    except Exception as e:
        return error_api(e.args)
