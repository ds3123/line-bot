# FastAPI
from fastapi import FastAPI, HTTPException
from fastapi.params import Header

# Line SDK
from linebot import LineBotApi , WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent , PostbackEvent , TextMessage , ImageMessage , FileMessage , LocationMessage

# 內建
import os
import re
from pathlib import Path
from dotenv import load_dotenv
from starlette.requests import Request
from fastapi.middleware.cors import CORSMiddleware



# 自訂
from models.message_request import MessageRequest
from skills import *
from skills import skills


# origins = [
#             # < 允許特定網域 >
#             "http://demo02.cchouse.com.tw",
#
#            ]


app.add_middleware(

    CORSMiddleware,
    allow_origins     = ["*"] ,
    allow_credentials = True ,     # 允許前端攜帶 Cookie ( Axios 也有類似設定 ) --> for JWT
    allow_methods     = ["*"] ,
    allow_headers     = ["*"] ,

)






# FastAPI 物件
app = FastAPI()


# 載入環境變數
load_dotenv()


# Token
line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
# Secret
handler      = WebhookHandler( os.getenv('LINE_CHANNEL_SECRET') )


# 匹配函式
def get_message( request : MessageRequest ) :

    for pattern , skill in skills.items() :
        if re.match( pattern , request.intent ):
            return skill( request )

    request.intent = '{not_match}'

    return skills['{not_match}']( request )


@app.post("/api/line")
async def callback( request : Request , x_line_signature : str = Header( None ) ) :

    body = await request.body()

    try :

        handler.handle( body.decode( "utf-8" ) , x_line_signature )

    except InvalidSignatureError :

        raise HTTPException( status_code = 400 , detail = "Invalid signature. Please check your channel access token/channel secret." )

    return 'OK'


# -----------------------

# 文字訊息
@handler.add( event = MessageEvent , message = TextMessage )
def handle_message( event ) :

    msg_request         = MessageRequest()
    msg_request.intent  = event.message.text
    msg_request.message = event.message.text
    msg_request.user_id = event.source.user_id

    # 根據訊息類型，匹配相對應 _ 處理函式
    func = get_message( msg_request )

    # 回應訊息
    line_bot_api.reply_message( event.reply_token , func )


# 圖片訊息
@handler.add( event = MessageEvent , message = ImageMessage )
def handle_image( event ) :

    # 取得 _ 訊息id
    message_id = event.message.id

    # 透過訊息 id，取得 Line Server 上的此圖片檔案
    message_content = line_bot_api.get_message_content( message_id )

    # 將圖片檔案存到程式伺服器 ( images 資料夾 )
    with open( Path( f'images/{ message_id }.jpg' ).absolute() , 'wb' ) as f :
        for chunk in message_content.iter_content() :
            f.write( chunk )


# 檔案訊息
# @handler.add( event = MessageEvent, message = FileMessage )
# def handle_message( event ) :
#
#     static_tmp_path = os.path.join(os.path.dirname(__file__), 'files')
#
#     message_content = line_bot_api.get_message_content(event.message.id)
#
#     with tempfile.NamedTemporaryFile(dir=static_tmp_path, prefix='file-', delete=False) as tf:
#         for chunk in message_content.iter_content():
#             tf.write(chunk)
#
#         tempfile_path = tf.name
#
#     dist_path = tempfile_path + '-' + event.message.file_name
#
#     dist_name = os.path.basename(dist_path)
#
#     os.rename(tempfile_path, dist_path)

# 定位
@handler.add( event = MessageEvent , message = LocationMessage )
def handle_message( event ) :

    print( 'location', event )
    print( '-----' )
    print( event.message.latitude )
    print( event.message.longitude )


# 接收資料
@handler.add( event = PostbackEvent )
def handle_message( event ) :

    print( 'postback' , event.postback )
    print( '-----' )
    print( 'params' , event.postback.params )
    print( 'data'   , event.postback.data )

