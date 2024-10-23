from functools import wraps

import aiohttp


class DictToObj:
    def __init__(self, dictionary):
        for key, value in dictionary.items():
            if isinstance(value, dict):
                setattr(self, key, DictToObj(value))
            elif isinstance(value, list):
                setattr(self, key, [DictToObj(item) if isinstance(item, dict) else item for item in value])
            else:
                setattr(self, key, value)

    def __repr__(self):
        return f"{self.__dict__}"

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
        data_as_obj = DictToObj(data)
        return await func(*args, response_data=data_as_obj, **kwargs)
    return wrapper
