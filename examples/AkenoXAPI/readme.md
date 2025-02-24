### FLUX-1SHELL
```py
from akenoai import AkenoXToJs

js = AkenoXToJs()

prompt = """
Lukisan airbrush abstrak setengah badan seorang pria Korea dengan rambut hitam berantakan,
mengenakan topeng hacker keren.
Jaket baseball merah dan putih bertuliskan 'MONYET' terlihat jelas. Gaya kontemporer, warna biru, kuning, dengan sentuhan sepia,
detail kode Python terukir di topeng
"""

response = await js.randydev.image.create(
    "black-forest-labs/flux-1-schnell",
    api_key="here", # @aknuserbot get api key
    image_read=True,
    query=prompt

file_path = "randydev.jpg"
with open(file_path, "wb") as f:
       f.write(response)
await message.reply_photo(file_path)
```
- [X] OUTPUT IMAGE
![Image](https://github.com/user-attachments/assets/78f22515-865f-4ea2-894c-c17cdd85364f)
### Story TG Downloader
```py
from akenoai import AkenoXToJs

js = AkenoXToJs()

await message.reply_video(
    await js.randydev.story_in_tg.download_story(
        api_key="your-api-key",
        link="https://t.me/KurimuzonAkuma/s/251"
    )
)
```
### Downloader
- [x] Instagram
- [x] Terabox
- [x] Facebook
- [x] XN*
- [x] all
```py
from akenoai import AkenoXToJs

js = AkenoXToJs()

download_response = await js.randydev.downloader.create(
    model="instagram-v4",
    api_key="<your-api-key-free>",
    is_obj=False,
    url="https://www.instagram.com/reel/DA0p2NoyN_O/?igsh=MWJvejMxZmZ5ZHd3YQ=="
)

return download_response
```
### AI & Models Premium
- [X] System Prompt
```py
from akenoai import AkenoXToJs

js = AkenoXToJs()

response = await js.randydev.chat.create(
    model="qwen/qwen1.5-1.8b-chat",
    api_key="<your-api-key-premium>",
    is_obj=True,
    query="Hello, how are you?"
)

return response
```
