### Game Random
```py
from akenoai import AkenoXToJs

js = AkenoXToJs(is_itzpire=True).connect()

response = await js.games.create("siapakah-aku", api_key="test", remove_author=True)
print(response)
```
### Object attributes
```py
from akenoai import AkenoXToJs

js = AkenoXToJs(is_itzpire=True).connect()

await js.chat.create(*args, **kwargs)
await js.anime.create(*args, **kwargs)
await js.downloader.create(*args, **kwargs)
await js.information.create(*args, **kwargs)
await js.maker.create(*args, **kwargs)
await js.movie.create(*args, **kwargs)
await js.random.create(*args, **kwargs)
await js.search.create(*args, **kwargs)
```
