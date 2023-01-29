from linebot.models import TemplateSendMessage
from linebot.models.template import ButtonsTemplate
from linebot.models.actions import MessageAction

from models.message_request import MessageRequest
from skills import add_skill


@add_skill( '查詢' )
def get( message_request : MessageRequest ) :

    buttons_template_message = TemplateSendMessage(

        alt_text = 'Buttons template' ,
        template = ButtonsTemplate(
                        thumbnail_image_url = 'https://diz36nn4q02zr.cloudfront.net/webapi/imagesV3/Original/SalePage/8227242/0/638055799480430000?v=1',
                        title   = ' 2023 包月方案查詢',
                        text    = '您可以查詢 :',
                        actions = [
                                    MessageAction(
                                        label = '包月使用方式',
                                        text  = '包月使用方式'
                                    ) ,
                                    MessageAction(
                                        label = '包月使用期限',
                                        text  = '包月使用期限'
                                    ) ,
                                    MessageAction(
                                        label = '剩餘額度',
                                        text  = '剩餘額度'
                                    ),
                                    MessageAction(
                                        label = '退款方式',
                                        text  = '退款方式'
                                    ),

                                  ]
                   )
    )

    return [ buttons_template_message ]




