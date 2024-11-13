from pyrogram.types import *


class BuilderInline:
    pass

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

def send_text_inline(photo_url, **args):
    answers = [
        InlineQueryResultPhoto(
            title="Error!",
            thumb_url="https://telegra.ph//file/586a3867c3e16ca6bb4fa.jpg",
            **args
        )
    ]
    return answers

def send_photo_inline(photo_url, **args):
    answers = [
        InlineQueryResultPhoto(
            title="Error!",
            thumb_url="https://telegra.ph//file/586a3867c3e16ca6bb4fa.jpg",
            **args
        )
    ]
    return answers

def send_video_inline(photo_url, **args):
    answers = [
        InlineQueryResultVideo(
            title="Error!",
            thumb_url="https://telegra.ph//file/586a3867c3e16ca6bb4fa.jpg",
            **args
        )
    ]
    return answers

def send_video_inline(photo_url, **args):
    answers = [
        InlineQueryResultVideo(
            title="Error!",
            thumb_url="https://telegra.ph//file/586a3867c3e16ca6bb4fa.jpg",
            **args
        )
    ]
    return answers
