from linebot.models import TemplateSendMessage
from linebot.models.template import ImageCarouselTemplate , ImageCarouselColumn
from linebot.models.actions import PostbackAction

from models.message_request import MessageRequest
from skills import add_skill


@add_skill( '{template-image-carousel}' )
def get( message_request : MessageRequest ) :

    image_carousel_template_message = TemplateSendMessage(

        alt_text = 'ImageCarousel template',
        template = ImageCarouselTemplate(
                        # columns 數最多 10 個
                        # 每個 column 中的 actions ，數目要一樣
                        columns = [
                                    ImageCarouselColumn(
                                                        image_url = 'https://s.yimg.com/ny/api/res/1.2/M4Gi7EZWnxMmnIYVnDH7fQ--/YXBwaWQ9aGlnaGxhbmRlcjt3PTk2MDtoPTY0MDtjZj13ZWJw/https://s.yimg.com/os/creatr-uploaded-images/2022-10/24067f40-4488-11ed-9bb7-657909af0c08',
                                                        action    = PostbackAction(
                                                                                    label        = '預 約',
                                                                                    display_text = 'postback text1',
                                                                                    data         = 'action=buy&itemid=1'
                                                                                   )
                                    ),
                                    ImageCarouselColumn(
                                                        image_url = 'https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2021/12/30/draft/14964211.jpg&x=0&y=0&sw=0&sh=0&sl=W&fw=800&exp=3600&w=465&nt=1',
                                                        action    = PostbackAction(
                                                                                    label        = 'postback2',
                                                                                    display_text = 'postback text2',
                                                                                    data         = 'action=buy&itemid=2'
                                                                                   )
                                    )
                                  ]
                   )

    )

    return [ image_carousel_template_message ]



