class OpenAI:
    @classmethod
    async def run(cls, key, openai_meta, model=None, messages=None, **args):
        try:
            client = openai_meta(
                api_key=key
            )
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                timeout=1.0,
                **args
            )
            return response
        except Exception as e:
            return f"Error response: {e}"
