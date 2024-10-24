from functools import wraps
import akeno.logger as akeno


def with_premium(func):
    async def wrapped(client, message):
        if not client.me.is_premium:
            await message.edit_text("<b>Premium account is required</b>")
        else:
            return await func(client, message)
    return wrapped

def LogChannel(is_track: bool: False, channel_id: int):
    def decorator(func):
        @wraps(func)
        async def wrapper(client, message):
            if is_track:
                try:
                    formatting = (
                        f"UserID: {message.from_user.id if message.from_user else 0}"
                        f"Username: {message.from_user.username if message.from_user else None}"
                        f"First Name: {message.from_user.first_name if message.from_user else ""}"
                    )
                    return await client.send_message(channel_id, formatting)
                except Exception as e:
                    await akeno.warning(str(e))
                return await func(client, message)
        return wrapper
    return decorator

def check_is_admin(status: bool = True):
    def decorator(func):
        @wraps(func)
        async def wrapper(client, message):
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
