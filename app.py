from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import requests, json


import errno
import os
import sys, random
import tempfile
import requests
import re

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent,
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('N+kb+5GOwEYqquNY+xjXzIcl0PoaSnPsbDUfrOQXct28PU9QCOSULzZPbjoShqtldj3x/XMnV9dPLv7Bt3oidelKN0M9HrXQVX29o76GQMvLg7oALZl1P0XOHKT3CEUse3TXDscrbf5qyBOy8PFYVQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('04b19507f4e25223b0ab0b12b05ea1b1')
#===========[ NOTE SAVER ]=======================
notes = {}

# Post Request
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text #simplify for receove message
    sender = event.source.user_id #get usesenderr_id
    gid = event.source.sender_id #get group_id
    profile = line_bot_api.get_profile(sender)
    if text=="Adit":
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Kamu jahat adit'))
    if text=="Mail":
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Kamu jahat mail'))
    if text=="Djohan":
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Kamu jahat djohan'))
    if text=="San Diego":
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='WATASHI WA NAMBA WAN !!!'))    

    
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Halo '+profile.display_name+'\nKata Kunci Tidak Diketahui :) \nKetik "menu" untuk mengetahui menu yang tersedia'))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)