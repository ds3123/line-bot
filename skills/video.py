

from linebot.models import VideoSendMessage
from models.message_request import MessageRequest
from skills import add_skill


@add_skill( '{video}' )
def get( message_request : MessageRequest ) :

    video_message = VideoSendMessage(
                        # 預覽影片 url
                        preview_image_url     = 'https://i.imgur.com/oLvTjtu.png' ,
                        # 原始影片 url
                        original_content_url  = 'https://i.imgur.com/n8QsXTk.mp4'
                     )

    return [ audio_message ]




