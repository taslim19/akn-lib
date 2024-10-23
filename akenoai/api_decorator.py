def my_api_anime(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        api_url = ""
        try:
            response = requests.post(api_url, json=kwargs)
            response.raise_for_status()
            data = response.json()
        except requests.RequestException as e:
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
