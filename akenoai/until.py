class LoopAutomatic:
    @classmethod
    async def start_running_loop(cls, sessions, ClientClass) -> None:
        for i, data in enumerate(sessions):
            yield i, data

    @classmethod        
    async def run_until_complete(
        cls,
        sessions,
        ClientClass,
        logs=None,
        my_api_id=None,
        my_api_hash=None,
        plugins_dir=None,
        is_token: bool = False,
    ) -> None:
        async for i, data in cls.start_running_loop(sessions, ClientClass):
            if is_token:
                bot_token_str = data.get("bot_token")
                client = ClientClass(
                    api_id=my_api_id,
                    api_hash=my_api_hash,
                    bot_token=bot_token_str,
                    plugins=dict(root=plugins_dir),
                )
            else:
                api_id = data.get("api_id")
                api_hash = data.get("api_hash")
                session_str = data.get("session")
                client = ClientClass(
                    api_id=api_id,
                    api_hash=api_hash,
                    session_string=session_str,
                    plugins=dict(root=plugins_dir)
                )
            
            await client.start()
            get_me = await client.get_me()
            if logs:
                logs.info(f"Starting: {i + 1} {get_me.first_name}")
            else:
                print(f"Starting: {i + 1} {get_me.first_name}")
