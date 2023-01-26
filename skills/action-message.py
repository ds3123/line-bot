from linebot.models import TemplateSendMessage
from linebot.models.template import ButtonsTemplate
from linebot.models.actions import MessageAction

from models.message_request import MessageRequest
from skills import add_skill


@add_skill( '{action-message}' )
def get( message_request : MessageRequest ) :

    msg = TemplateSendMessage(
                                alt_text = 'Actions',
                                template = ButtonsTemplate(
                                                title   = '方案選項 :',
                                                text    = '請點選',
                                                actions = [
                                                            MessageAction(
                                                                           label = '點我，看貼圖 _ 1',
                                                                           text  = '{sticker}'  # 點選後，再進一步看貼圖
                                                                          ) ,
                                                            MessageAction(
                                                                            label='點我，看貼圖 _ 2',
                                                                            text='{sticker}'
                                                            ),

                                                          ]
                                            )
                             )

    return [ msg ]




