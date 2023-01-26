
from linebot.models import ImageSendMessage
from models.message_request import MessageRequest
from skills import add_skill


@add_skill( '{image}' )
def get( message_request : MessageRequest ) :


    img_message = ImageSendMessage(
                     # 預覽圖 url
                     preview_image_url    = 'https://via.placeholder.com/800x600/333.png/fff' ,
                     # 原始圖 url
                     original_content_url = 'https://via.placeholder.com/1024x768/333.png/fff'
                  )

    return [ img_message ]



