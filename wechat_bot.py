import itchat
import requests

# 这里换成你的 Mistral API Key
MISTRAL_API_KEY = "U7Vm2lwNoDDQjj38UK1mjCAjrGWgJmUh"  # 请替换为你的 Mistral API Key

def get_mistral_reply(user_msg):
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistral-medium",  # 选择模型
        "messages": [{"role": "user", "content": user_msg}]
    }
    response = requests.post("https://api.mistral.ai/v1/chat/completions", json=data, headers=headers)
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return "抱歉，我暂时无法回复。"

itchat.auto_login(hotReload=True)

@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def group_reply(msg):
    if msg['isAt']:  # 只有被 @ 时才回复
        user_msg = msg['Text']
        sender_name = msg['ActualNickName']

        reply = get_mistral_reply(user_msg)
        reply_text = f"@{sender_name} {reply}"
        itchat.send(reply_text, toUserName=msg['FromUserName'])

itchat.run()
