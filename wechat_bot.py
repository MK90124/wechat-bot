import itchat
import openai

openai.api_key = "你的 OpenAI API Key"

itchat.auto_login(hotReload=True)

@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def group_reply(msg):
    if msg['isAt']:  # 只有被 @ 时才回复
        user_msg = msg['Text']
        sender_name = msg['ActualNickName']

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_msg}]
            )
            reply = response["choices"][0]["message"]["content"]
        except:
            reply = "抱歉，我暂时无法回复，请稍后再试。"

        reply_text = f"@{sender_name} {reply}"
        itchat.send(reply_text, toUserName=msg['FromUserName'])

itchat.run()
