
from linebot.models import TextSendMessage
from models.message_request import MessageRequest
from skills import add_skill


@add_skill( '{text}' )
def get( message_request : MessageRequest ) :

    # 文字訊息
    msg_1 = TextSendMessage( text = 'Hello Text_1' )
    msg_2 = TextSendMessage( text = 'Hello Text_2' )

    # Emoji 訊息
    txt   = '$ LINE emoji $'
    emoji = [
                {
                    "index": 0,
                    "productId": "5ac1bfd5040ab15980c9b435",
                    "emojiId": "001"
                },
                {
                    "index": 13,
                    "productId": "5ac1bfd5040ab15980c9b435",
                    "emojiId": "002"
                }
             ]

    emoji_message = TextSendMessage( text = '$ LINE emoji $', emojis = emoji )

    return [ msg_1 , msg_2 , emoji_message ]












