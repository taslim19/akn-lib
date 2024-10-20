import base64

class OpenAI:
    api_key = ""

    @classmethod
    def set_api_key(cls, key=Ellipsis):
        if key is Ellipsis:
            cls.api_key = base64.b64decode("c2stcHJvai1TT0ZUQjRkRDUxdFl4OWIzZkUxaVQzQmxia0ZKUmhlT1FKYUxoNW44aHB3YXpoUWs=").decode("utf-8")
        elif not key:
            raise ValueError("API key must be provided!")
        else:
            cls.api_key = key

    @classmethod
    async def run_image(
        cls,
        key=Ellipsis,
        openai_meta=None,
        run_async: bool = False,
        **args
    ):
        cls.set_api_key(key)
        try:
            client = openai_meta(api_key=cls.api_key)
            if run_async:
                response = await client.images.generate(
                    model="dall-e-3",
                    **args
                )
            else:
                response = client.images.generate(
                    model="dall-e-3",
                    **args
                )
            return response.data[0].url if response and response.data else ""
        except Exception as e:
            return f"Error response: {e}"

    @classmethod
    async def run(
        cls,
        key=Ellipsis,
        openai_meta=None,
        model=None,
        messages=None,
        async_is_stream: bool = False,
        **args
    ):
        cls.set_api_key(key)
        try:
            client = openai_meta(api_key=cls.api_key)
            if async_is_stream:
                answer = ""
                response_stream = await client.chat.completions.create(
                    model=model,
                    messages=messages,
                    **args
                )
                async for chunk in response_stream:
                    answer += chunk.choices[0].delta.content or ""
                return answer
            else:
                response = await client.chat.completions.create(
                    model=model,
                    messages=messages,
                    **args
                )
                return response.choices[0].message.content or ""
        except Exception as e:
            return f"Error response: {e}"
