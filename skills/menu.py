from linebot.models import TemplateSendMessage
from linebot.models.template import ImageCarouselTemplate , ImageCarouselColumn
from linebot.models.actions import MessageAction

from models.message_request import MessageRequest
from skills import add_skill

# @ 服務選項清單
@add_skill( 'm' )
def get( message_request : MessageRequest ) :

    image_carousel_template_message = TemplateSendMessage(

        alt_text = 'ImageCarousel template',
        template = ImageCarouselTemplate(


                        # 預約
                        columns = [

                                    ImageCarouselColumn(
                                        image_url='https://s.yimg.com/ny/api/res/1.2/M4Gi7EZWnxMmnIYVnDH7fQ--/YXBwaWQ9aGlnaGxhbmRlcjt3PTk2MDtoPTY0MDtjZj13ZWJw/https://s.yimg.com/os/creatr-uploaded-images/2022-10/24067f40-4488-11ed-9bb7-657909af0c08',
                                        action = MessageAction(
                                                        label = '~ 預 約 ~',
                                                        text  = '預約'
                                                    )

                                    ) ,

                                    ImageCarouselColumn(
                                        image_url = 'https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2021/12/30/draft/14964211.jpg&x=0&y=0&sw=0&sh=0&sl=W&fw=800&exp=3600&w=465&nt=1',
                                        action    =  MessageAction(
                                                        label = '~ 查 詢 ~',
                                                        text  = '查詢'
                                                     )

                                    ) ,

                                    ImageCarouselColumn(
                                        image_url='https://www.pet100pa.com//goll_tw/ckfinder/userfiles/images/%E4%B8%8B%E8%BC%89%20(1).jpg',
                                        action=MessageAction(
                                            label='~ Q & A ~',
                                            text='Q&A'
                                        )

                                    ),


                                ]
                  )

    )

    return [ image_carousel_template_message ]



