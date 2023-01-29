from linebot.models import TemplateSendMessage
from linebot.models.template import CarouselTemplate , CarouselColumn
from linebot.models.actions import MessageAction , URIAction

from models.message_request import MessageRequest
from skills import add_skill


# 預約 _ 服務選項
@add_skill( '預約' )
def get( message_request : MessageRequest ) :

    carousel_template_message = TemplateSendMessage(

        alt_text = '預約服務',
        template = CarouselTemplate(

            columns=[
                        CarouselColumn(
                            thumbnail_image_url='https://s.yimg.com/ny/api/res/1.2/M4Gi7EZWnxMmnIYVnDH7fQ--/YXBwaWQ9aGlnaGxhbmRlcjt3PTk2MDtoPTY0MDtjZj13ZWJw/https://s.yimg.com/os/creatr-uploaded-images/2022-10/24067f40-4488-11ed-9bb7-657909af0c08',
                            title = '洗 澡',
                            text  = '一 ~ 五 ( 09:00 AM ~ 09:00 PM )',
                            actions = [
                                        MessageAction(
                                            label = '預約 _ 洗澡',
                                            text  = '預約洗澡'
                                        )

                                        # URIAction(
                                        #            label = "預約 _ 洗澡" ,
                                        #            uri   = 'https://liff.line.me/1657852584-wXk5JR18'
                                        #          )

                                      ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url='https://images.chinatimes.com/newsphoto/2021-03-13/1024/20210313002620.jpg',
                            title   = '美 容',
                            text    = '一 ~ 五 ( 09:00 AM ~ 09:00 PM )',
                            actions = [
                                          MessageAction(
                                              label = '預約 _ 美容',
                                              text  = '預約美容'
                                          )
                                      ]
                        ) ,
                        CarouselColumn(
                            thumbnail_image_url='https://clairetila.com/wp-content/uploads/20191006214007_71.jpg',
                            title   = '安 親',
                            text    = '一 ~ 五 ( 09:00 AM ~ 09:00 PM )',
                            actions = [
                                MessageAction(
                                    label = '預約 _ 安親',
                                    text  = '預約安親'
                                )
                            ]
                        ) ,
                        CarouselColumn(
                            thumbnail_image_url='https://www.niusnews.com/upload/imgs/default/202207_Jennie/0728hotel/02.jpeg',
                            title   = '住 宿',
                            text    = '一 ~ 五 ( 09:00 AM ~ 09:00 PM )',
                            actions = [
                                MessageAction(
                                    label = '預約 _ 住宿',
                                    text  = '預約住宿'
                                )
                            ]
                        )


            ]
        )
    )

    return [carousel_template_message]




