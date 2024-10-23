def with_premium(func):
    async def wrapped(client, message):
        if not client.me.is_premium:
            await message.edit_text("<b>Premium account is required</b>")
        else:
            return await func(client, message)
    return wrapped

def check_is_admin(func):
    async def wrapped(client, message):
        pass
      return await func(client, message)
    return wrapped
