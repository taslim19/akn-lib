def with_premium(func):
    async def wrapped(client, message):
        if not client.me.is_premium:
            await message.edit_text("<b>Premium account is required</b>")
        else:
            return await func(client, message)
    return wrapped

def check_is_admin(status: bool = True, enums=None):
    def decorator(func):
        @wraps(func)
        async def wrapper(client, message):
            if status:
                member = await client.get_chat_member(message.chat.id, "me")
                if not member.status == enums.ChatMemberStatus.ADMINISTRATOR:
                    await message.reply_text("I am not an administrator in this group")
                else:
                    return await func(client, message)
            else:
                return "Status False ADMINISTRATOR"
        return wrapper
    return decorator
