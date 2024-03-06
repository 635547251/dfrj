import requests

# Function to send a message to Dify
def dify_mbti(
        query, 
        conversation_id, 
        user,
        api_url,
        api_key
    ):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        'inputs':{
            "persona":"infj"
        },
        'query':query,
        'response_mode':'streaming',
        'conversation_id': conversation_id,
        'user': user
    }
    response = requests.post(api_url+'/chat-messages', headers=headers, json=data, stream=True)
    return response

'''
data: {"event": "message", "task_id": "900bbd43-dc0b-4383-a372-aa6e6c414227", "id": "663c5084-a254-4040-8ad3-51f2a3c1a77c", "answer": "Hi", "created_at": 1705398420}
'''