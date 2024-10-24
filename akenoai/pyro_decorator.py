from functools import wraps
import akenoai.logger as akeno

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus

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

def LogChannel(channel_id=None, is_track: bool = False):
    def decorator(func):
        @wraps(func)
        async def wrapper(client: Client, message: Message):
            if is_track:
                try:
                    formatting = (
                        f"UserID: {message.from_user.id if message.from_user else 0}\n"
                        f"Username: {message.from_user.username if message.from_user else None}\n"
                        f"First Name: {message.from_user.first_name if message.from_user else ''}\n"
                    )
                    await client.send_message(channel_id, formatting)
                except Exception as e:
                    await akeno.warning(str(e))
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
