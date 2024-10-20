class OpenAI:
    @classmethod
    def set_api_key(cls, key, openai_meta):
        openai_meta.api_key = key

    @classmethod
    async def run(cls, key, openai_meta, model=None, messages=None, **args):
        try:
            cls.set_api_key(key, openai_meta)
            response = openai_meta.ChatCompletion.create(
                model=model,
                messages=messages,
                timeout=1.0,
                **args
            )
            return response["choices"][0]["message"]["content"]
        except Exception as e:
            return f"Error response: {e}"
