from typing import Text
from linebot.models import TextSendMessage
from models.message_request import MessageRequest
from skills import add_skill


# 沒有符合特定指令字串，即回覆 _ 使用者所輸入字串
@add_skill( '{not_match}' )
def get( message_request : MessageRequest) :

    return [
              TextSendMessage( text = f'您輸入 ： { message_request.message }' )
           ]
