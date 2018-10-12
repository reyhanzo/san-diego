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

def inputgame(Judul, Tahun, Genre, OS):
    r = requests.post("http://www.aditmasih.tk/api_reyreyrey/insert.php", data={'judul': Judul, 'tahun': Tahun, 'genre': Genre, 'os': OS})
    data = r.json()
    # return data
    flag = data['flag']
    return flag
    
    if(flag == "1"):
        return 'Data '+nama+' berhasil dimasukkan dan tersimpan\n'
    elif(flag == "0"):
        return 'Data gagal dimasukkan, coba tanya yg buat kenapa...\n'

def carigame(Judul):
    URLgame = "http://www.aditmasih.tk/api_reyreyrey/show.php?judul=" + Judul
    r = requests.get(URLgame)
    data = r.json()
    err = "data tidak ditemukan :("
    
    flag = data['flag']
    if(flag == "1"):
        Judul = data['data_game'][0]['judul']
        Tahun = data['data_game'][0]['tahun']
        Genre = data['data_game'][0]['genre']
        OS = data['data_game'][0]['os']

        # munculin semua, ga rapi, ada 'u' nya
        # all_data = data['data_angkatan'][0]
        data= "Judul : "+Judul+"\nTahun : "+Tahun+"\nGenre : "+Genre+"\nOS : "+OS
        return data
        # return all_data

    elif(flag == "0"):
        return err


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text #simplify for receove message
    sender = event.source.user_id #get usesenderr_id
    gid = event.source.sender_id #get group_id
    profile = line_bot_api.get_profile(sender)
    data=text.split('-')
    if(data[0]=='Tambah'):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=inputgame(data[1],data[2],data[3],data[4])))
    if(data[0]=='Lihat'):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=carigame(data[1])))
    if text=="Description":
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Atlanta-class Light Cruiser-San Diego, Hull number CL-53 '))
    if text=="I love you":
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I love you too, because We are Number One.'))
    if text=="San Diego":
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='WATASHI WA NAMBA WAN !!!'))    
    if text=="Rate":
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Super Rare, and The best Light Cruiser in the World !!!'))
    if text=="Best Pose":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url='https://azurlane.koumakan.jp/w/images/d/d8/San_Diego.png',preview_image_url='https://azurlane.koumakan.jp/w/images/d/d8/San_Diego.png'))
    if text=="Miku":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url='https://eimusics.com/wp-content/uploads/2015/02/2013.03.20-livetune-feat.-Hatsune-Miku-Redial-1280x720-H264-AAC-eimusics.com_.mkv_snapshot_00.02_2015.02.19_11.33.51.jpg',
    preview_image_url='https://eimusics.com/wp-content/uploads/2015/02/2013.03.20-livetune-feat.-Hatsune-Miku-Redial-1280x720-H264-AAC-eimusics.com_.mkv_snapshot_00.02_2015.02.19_11.33.51.jpg'))    
    if text=="Menu":
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Description, I love you, San Diego, Rate, Best Pose, Miku, Belfast'))    
    if text=="Belfast":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url='https://archive.hnsa.org/ships/img/belfast1.jpg',preview_image_url='https://archive.hnsa.org/ships/img/belfast1.jpg'))


    line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Ngapain Kamu '+profile.display_name+'\nNulis apa kamu \nKetik "Menu" woi....'))


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)