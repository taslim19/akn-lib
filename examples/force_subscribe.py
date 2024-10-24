# pip3 install git+https://github.com/TeamKillerX/akenoai-lib
# pip3 install pyrogram or pyrofork
# pip3 install RyuzakiLib[all]
# Force subscribe channel powered by @xtdevs
# remember: you add bot to channel as admin

from pyrogram import Client, filters
from pyrogram.types import *

import akenoai.pyro_decorator as akeno

force_sub = akeno.ForceSubscribe(where_from="RendyProjects", owner_id="xtdevs")

@Client.on_message(
    filters.incoming
    & filters.private
    & filters.command(["start"])
    & ~filters.forwarded,
    group=2,
)
@force_sub
async def startbot(client: Client, message: Message):
    buttons = [
        [
            InlineKeyboardButton(
                text="Developer",
                url=f"https://t.me/xtdevs"
            ),
            InlineKeyboardButton(
                text="Channel",
                url='https://t.me/RendyProjects'
            ),
        ],
    ]
    await message.reply_text(
        text=f"Hello {message.from_user.mention}\nJoin Channel",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(buttons)
    )

@Client.on_message(
    filters.incoming
    & filters.command(["help"])
    & ~filters.forwarded
)
@force_sub
async def helpcmd(client: Client, message: Message):
    await message.reply_text("Good Joined Channel")
