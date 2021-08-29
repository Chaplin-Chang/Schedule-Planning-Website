from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,SourceUser,StickerSendMessage,TemplateSendMessage,ImagemapSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('mhDgsL1co2B6zyMqPROBjA854E+lyLpx/1BVkyrGN+U/eXlZxn/lY2ytGNxuDWXeW8Xn2p8PTXOSLV4L9JRKWkYQFcuU55/BoNp3qpK+QDbFYaVrN8qq2ZQmcYLuNc9doULqj5g3c3hmYyCtX0xGQwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('0ed4045d630e8bd06f997333ffcc7e72')

user=[]

@app.route("/pish",methods=['GET'])
def pushmessage():
    for uid in users:
        line_bot_api.push_message(uid, TextSendMessage(text='Hello World!'))
    return "push user# " + str(len(users))+" OK"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text=event.message.text
    if text =='My Booking':
        message = 'check this adress'
        line_bot_api.reply_message(event.reply_token, message)

    else:
        message = StickerSendMessage(
            package_id='1',
            sticker_id='1'
        )
        line_bot_api.reply_message(event.reply_token, message)

if __name__ == "__main__":
    app.run()