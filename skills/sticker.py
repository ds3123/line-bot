from linebot.models import TemplateSendMessage , StickerSendMessage
from linebot.models.template import ButtonsTemplate
from linebot.models.actions import MessageAction

from models.message_request import MessageRequest
from skills import add_skill


@add_skill( '{sticker}' )
def get( message_request : MessageRequest ) :

    sticker = StickerSendMessage( package_id = 789 , sticker_id = 10855 )

    return [ sticker ]



