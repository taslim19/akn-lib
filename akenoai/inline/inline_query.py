from pyrogram.types import *

def inline_error(inline_text, **args):
    answers = [
        InlineQueryResultArticle(
            title="Error!",
            thumb_url="https://telegra.ph//file/586a3867c3e16ca6bb4fa.jpg",
            input_message_content=InputTextMessageContent(
                message_text=inline_text,
                disable_web_page_preview=True
            ),
            **args
        )
    ]
    return answers
