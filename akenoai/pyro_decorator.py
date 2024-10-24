# MODULES MOD
# FULL CREDITS BY @XTDEVS  
# PLEASE DO NOT REMOVE CREDITS  
# COPYRIGHT 2019-2024
# REMEMBER: COPYING AND PASTING WITHOUT UNDERSTANDING WILL ONLY HURT YOUR GROWTH. RESPECT THE ORIGINAL WORK BY GIVING PROPER CREDITS AND FOLLOWING THE RULES. START LEARNING, NOT JUST COPYING!

from functools import wraps

from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message
from pyrogram.errors import *

import akenoai.logger as akeno

def ForceSubscribe(where_from=None, owner_id=None):
    def decorator(func):
        @wraps(func)
        async def wrapper(client: Client, message: Message):
            try:
                if "https://t.me/" in where_from:
                    return await client.send_message(owner_id, "Please Don't link: format eg: where_from='RendyProjects'")
                if not (await check_membership(where_from, owner_id, client, message)):
                    force_button = InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    text="The Channel",
                                    url=f"https://t.me/{where_from}"
                                )
                            ]
                        ]
                    )
                    mention = message.from_user.mention if message.from_user else ""
                    user_id = message.from_user.id if message.from_user else 0
                    await message.reply(
                        f"Hey {mention}\n⚠️ To use this bot you have to <b>subscribe to our channel</b>",
                        disable_web_page_preview=True,
                        reply_markup=force_button
                    )
                    await message.stop_propagation()
            except ChatAdminRequired as e:
                await akeno.warning(str(e))
            return await func(client, message)
        return wrapper
    return decorator

async def check_membership(channel_id, owner, bot, msg):
    try:
        user_id = msg.from_user.id if msg.from_user else 0
        mention_user = await bot.get_users(user_id)
        user = await bot.get_chat_member(channel_id, user_id)
        if user.status == ChatMemberStatus.BANNED:
            admin_support = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Developer",
                            url=f"https://t.me/{owner}"
                        )
                    ]
                ]
            )
            mention = mention_user.mention if mention_user else ""
            await bot.send_message(
                msg.chat.id,
                text=f"❌ you {mention} have been blocked from the group support\n\nclick the button below to contact the group admin",
                reply_markup=admin_support
            )
            return False
        return True
    except UserNotParticipant:
        return False

def with_premium(func):
    async def wrapper(client: Client, message: Message):
        if not client.me.is_premium:
            await message.edit_text("<b>Premium account is required</b>")
        else:
            return await func(client, message)
    return wrapper

def disable_command(command=None):
    def decorator(func):
        @Client.on_message(~filters.command(command))
        async def wrapper(client: Client, message: Message):
            await func(client, message)
        return wrapper
    return decorator

def format_user_info(user) -> str:
    return (
        f"UserID: {user.id if user else 0}\n"
        f"Username: {user.username if user else None}\n"
        f"First Name: {user.first_name if user else ''}\n"
    )

def LogChannel(channel_id=None, is_track: bool = False):
    def decorator(func):
        @wraps(func)
        async def wrapper(client: Client, message: Message):
            if is_track:
                try:
                    formatting = format_user_info(message.from_user)
                    await client.send_message(channel_id, formatting)
                except Exception as e:
                    await akeno.warning(str(e))
            else:
                return False
            return await func(client, message)
        return wrapper
    return decorator

def check_is_admin(status: bool = True):
    def decorator(func):
        @wraps(func)
        async def wrapper(client: Client, message: Message):
            if status:
                try:
                    member = await client.get_chat_member(message.chat.id, "me")
                    if member.status != ChatMemberStatus.ADMINISTRATOR:
                        return await message.reply_text("I am not an administrator in this group.")
                except Exception as e:
                    return await message.reply_text(f"Error while checking admin status: {e}")
                return await func(client, message)
            else:
                return await message.reply_text("Admin check is disabled.")
        return wrapper
    return decorator
