from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES


def error_response(status_code, message=None):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response


def bad_request(message):
    '''最常用的错误 400：错误的请求'''
    return error_response(400, message)

def error_parameter(parameter):
    '''提问的参数缺少'''
    payload = {'error': f'缺乏必要的参数:{parameter}'}
    response = jsonify(payload)
    response.status_code = 401
    return response

def error_api(api_error):
    '''提问的参数缺少'''
    payload = {'error': f'接口报错:{api_error}'}
    response = jsonify(payload)
    response.status_code = 402
    return response