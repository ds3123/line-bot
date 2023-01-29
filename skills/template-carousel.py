from linebot.models import TemplateSendMessage
from linebot.models.template import CarouselTemplate , CarouselColumn
from linebot.models.actions import MessageAction

from models.message_request import MessageRequest
from skills import add_skill


@add_skill( '{template-carousel}' )
def get( message_request : MessageRequest ) :

    carousel_template_message = TemplateSendMessage(

        alt_text = 'Carousel template',
        template = CarouselTemplate(
                        # columns 數最多 10 個
                        # 每個 column 中的 actions ，數目要一樣
                        columns = [
                                    CarouselColumn(
                                        thumbnail_image_url = 'https://s.yimg.com/ny/api/res/1.2/M4Gi7EZWnxMmnIYVnDH7fQ--/YXBwaWQ9aGlnaGxhbmRlcjt3PTk2MDtoPTY0MDtjZj13ZWJw/https://s.yimg.com/os/creatr-uploaded-images/2022-10/24067f40-4488-11ed-9bb7-657909af0c08',
                                        title               = 'this is menu1',
                                        text                = 'description1',
                                        actions             = [
                                                                MessageAction(
                                                                    label = 'message1',
                                                                    text  = 'message text1'
                                                                )
                                                               ]
                                    ) ,
                                    CarouselColumn(
                                        thumbnail_image_url = 'https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2021/12/30/draft/14964211.jpg&x=0&y=0&sw=0&sh=0&sl=W&fw=800&exp=3600&w=465&nt=1',
                                        title               = 'this is menu2',
                                        text                = 'description2',
                                        actions             = [
                                                                MessageAction(
                                                                    label = 'message2',
                                                                    text  = 'message text2'
                                                                )
                                                              ]
                                    )
                                  ]
                  )
    )

    return [ carousel_template_message ]



