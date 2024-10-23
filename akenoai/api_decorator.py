import aiohttp

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
        return func(*args, response_data=data, **kwargs)
    return wrapper

def my_api_ping(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        api_url = ""
        try:
            response = requests.get(api_url, params=kwargs)
            response.raise_for_status()
            data = response.json()
        except requests.RequestException as e:
            return f"API Error: {str(e)}"
        return func(*args, response_data=data, **kwargs)
    return wrapper
