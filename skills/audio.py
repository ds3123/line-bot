
from linebot.models import AudioSendMessage
from models.message_request import MessageRequest
from skills import add_skill


@add_skill( '{audio}' )
def get( message_request : MessageRequest ) :

    audio_message = AudioSendMessage(
                        # 音檔 url
                        original_content_url = 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3',
                        # 播放時間 : 60秒
                        duration             = 60000
                    )

    return [ audio_message ]








