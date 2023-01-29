from linebot.models import TemplateSendMessage
from linebot.models.template import ButtonsTemplate
from linebot.models.actions import MessageAction

from models.message_request import MessageRequest
from skills import add_skill


@add_skill( 'Q&A' )
def get( message_request : MessageRequest ) :

    buttons_template_message = TemplateSendMessage(

        alt_text = 'Buttons template' ,
        template = ButtonsTemplate(
                        thumbnail_image_url = 'https://www.pet100pa.com//goll_tw/ckfinder/userfiles/images/%E4%B8%8B%E8%BC%89%20(1).jpg',
                        title   = '簡易問答',
                        text    = '您可以詢問 :',
                        actions = [
                                    MessageAction(
                                        label = '各項服務價格',
                                        text  = '各項服務價格'
                                    ) ,
                                    MessageAction(
                                        label = '是否有接送服務',
                                        text  = '是否有接送服務'
                                    ) ,
                                    MessageAction(
                                        label = '服務注意事項',
                                        text  = '服務注意事項'
                                    ),
                                    MessageAction(
                                        label = '服務時段與店家位置',
                                        text  = '服務時段與店家位置'
                                    ),

                                  ]
                   )
    )

    return [ buttons_template_message ]




