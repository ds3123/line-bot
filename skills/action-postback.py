
from linebot.models import TemplateSendMessage
from linebot.models.template import ButtonsTemplate
from linebot.models.actions import PostbackAction

from models.message_request import MessageRequest
from skills import add_skill


@add_skill( '{action-postback}' )
def get( message_request : MessageRequest ) :

    msg = TemplateSendMessage(
                                alt_text = 'Actions',
                                template = ButtonsTemplate(
                                                             title   = '資料內容',
                                                             text    = '選項',
                                                             actions = [
                                                                         PostbackAction( label = "送出" , data = "1" )
                                                                       ]
                                                           )
                              )

    return [ msg ]




