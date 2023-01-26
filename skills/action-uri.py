from linebot.models import TemplateSendMessage
from linebot.models.template import ButtonsTemplate
from linebot.models.actions import URIAction

from models.message_request import MessageRequest
from skills import add_skill


@add_skill( '{action-uri}' )
def get( message_request : MessageRequest ) :

    msg = TemplateSendMessage(
                               alt_text = 'Actions',
                               template = ButtonsTemplate(
                                                title   = '相關資訊',
                                                text    = '請點選',
                                                actions = [
                                                            URIAction(
                                                                       label = 'Google',
                                                                       # ?openExternalBrowser=1 手機以使用者預設瀏覽器開啟 ( 非 Line 內建 )
                                                                       uri   = 'https://www.google.com.tw/?openExternalBrowser=1'
                                                                      )
                                                          ]
                                           )
                              )


    return [ msg ]
