class OpenAI:
    @classmethod
    async def run(
        cls,
        key,
        openai_meta,
        model=None,
        messages=None,
        async_is_stream: bool = False,
        **args
    ):
        try:
            client = openai_meta(
                api_key=key
            )
            if async_is_stream:
                answer = ""
                response = await client.chat.completions.create(
                    model=model,
                    messages=messages,
                    **args
                )
                async for chunk in stream:
                    answer += chunk.choices[0].delta.content or ""
                return answer
            else:
                response = await client.chat.completions.create(
                    model=model,
                    messages=messages,
                    **args
                )
                return response
        except Exception as e:
            return f"Error response: {e}"
