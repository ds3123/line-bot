from linebot.models import TemplateSendMessage
from linebot.models.template import ButtonsTemplate
from linebot.models.actions import MessageAction

from models.message_request import MessageRequest
from skills import add_skill



@add_skill( '{template-button}' )
def get( message_request : MessageRequest ) :

    buttons_template_message = TemplateSendMessage(

        alt_text = 'Buttons template' ,
        template = ButtonsTemplate(
                        thumbnail_image_url = 'https://via.placeholder.com/300x300/333.png/fff',
                        title   = 'Menu',
                        text    = 'Please select',
                        actions = [
                                    MessageAction(
                                        label = 'carousel',
                                        text  = '{template-carousel}'
                                    ) ,
                                    MessageAction(
                                        label = 'image-carousel',
                                        text  = '{template-image-carousel}'
                                    ),
                                  ]
                   )
    )

    return [ buttons_template_message ]




