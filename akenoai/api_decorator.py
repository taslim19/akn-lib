import aiohttp
from functools import wraps

def my_api_chatgpt_old(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        api_url = "https://private-akeno.randydev.my.id/ryuzaki/chatgpt-old"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(api_url, json=kwargs) as response:
                    data = await response.json()
        except Exception as e:
            return f"API Error: {str(e)}"
        return await func(*args, response_data=data, **kwargs)
    return wrapper
