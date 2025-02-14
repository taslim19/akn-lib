# akenoai-lib
[![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.png?v=103)](https://github.com/TeamKillerX/akenoai-lib)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-Yes-green)](https://github.com/TeamKillerX/akenoai-lib/graphs/commit-activity)
[![GitHub Forks](https://img.shields.io/github/forks/TeamKillerX/akenoai-lib?&logo=github)](https://github.com/TeamKillerX/akenoai-lib)
[![GitHub Stars](https://img.shields.io/github/stars/TeamKillerX/akenoai-lib?&logo=github)](https://github.com/TeamKillerX/akenoai-lib/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/TeamKillerX/akenoai-lib?&logo=github)](https://github.com/TeamKillerX/akenoai-lib)
[![Size](https://img.shields.io/github/repo-size/TeamKillerX/akenoai-lib?color=green)](https://github.com/TeamKillerX/akenoai-lib)
[![Contributors](https://img.shields.io/github/contributors/TeamKillerX/akenoai-lib?color=green)](https://github.com/TeamKillerX/akenoai-lib/graphs/contributors)
[![License](https://img.shields.io/badge/License-GPL-pink)](https://github.com/TeamKillerX/akenoai-lib/blob/main/LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://makeapullrequest.com)
[![akenoai - Version](https://img.shields.io/pypi/v/akenoai?style=round)](https://pypi.org/project/akenoai)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/akenoai?label=DOWNLOADS&style=round)](https://pypi.org/project/akenoai)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/TeamKillerX/akenoai-lib/main.svg)](https://results.pre-commit.ci/latest/github/TeamKillerX/akenoai-lib/main)

### installation
🔹 <b>Recommended Installation:</b>

✅ Install via [`PYPI`](https://pypi.org/project/akenoai) for the latest updates. e.g.: `pip3 install akenoai[fast]`

✅ Install via github
- Create a requirements.txt file in the project root containing the following dependency to ensure you can install the GitHub version:
- `git+https://github.com/TeamKillerX/akenoai-lib.git#egg=akenoai[fast]`

### FastAPI Demo
- Use `main.py`
- Try running `python3 main.py`
```py
from akenoai.runner import run_fast

# run_fast initializes a FastAPI server with example routes and configurations.

run_fast()
```

### Code examples
> [!TIP]
> Trip PRO Usage Example:

- Use Access API key V2 Premium
```py
import json
from akenoai import AkenoXToJs

chat_history = [
    {"role": "User", "message": "hello world"},
    {"role": "Chatbot", "message": "Hello! How can I assist you today?"}
]

response = await AkenoXToJs.randydev(
    "ai/cohere/command-plus",
    api_key="<your_api_key>",
    custom_dev_fast=True,
    query="what is AkenoX AI?",
    chatHistory=json.dumps(chat_history),
    system_prompt="You are a helpful AI assistant designed to provide clear and concise responses."
)

print(response)
```
### 🌐 Streamlit + AkenoX API
- installation: `pip3 install akenoai[streamlit]`
- You can use `streamlit run app.py`
- `akenoai[fast]` → <b>Pyrogram error:</b> *There is no current event loop* (<b>Stuck in Streamlit</b>)

- Example usage:
```py
from akenoai import AkenoXToJs as js

js_st = js.stl()
js_st.title("Welcome to akenoai-lib APP")
js_st.write("Developed by RandyDev")
js_st.write("Example JSON")

with js_st.form("json"):
    submitted = js_st.form_submit_button("Submit")
    if submitted:
        js_st.spinner("Fetching data...")
        js_st.json(
            js.no_async_randydev("json/all", post=False, is_obj=False)
        )

js.hide_streamlit_watermark(unsafe_allow_html=True)
```
- [X] If using API `[fast]` for <b>full-stack</b>, move to `akenoai.clients`:
```py
from akenoai.clients import create_pyrogram # Use [fast]
```
### 🚀 Super-Fast Performance
Use AkenoX API + FastAPI
> [!WARNING]
> AkenoX API <b>may block access if there are too many spam requests!</b> 🚨
>
> Always use <b>rate limiting</b>
>
```py
from akenoai import AkenoXToJs as js
from akenoai.runner import run_fast

fast_app = js.get_app()
js.add_cors_middleware()

@fast_app.get("/api/cohere")
async def cohere(query: str):
    return await js.randydev(
        "ai/cohere/command-plus",
        api_key="<your_api_key>",
        custom_dev_fast=True,
        query=query,
        chatHistory=[],
        system_prompt="You are a helpful AI assistant designed to provide clear and concise responses."
    )

@fast_app.get("/test")
async def example_json():
    async with js.fasthttp().ClientSession() as session:
        async with session.get("https://jsonplaceholder.typicode.com/todos/1") as response:
            title = js.dict_to_obj(await response.json()).title
    return {"message": title}

run_fast(build=fast_app)
```
### 🛠️ Custom OpenAI
```py
from akenoai import AkenoXToJs as js

fast_app = js.get_app()

js.custom_openapi(
    app=fast_app,
    logo_url="https://github-production-user-asset-6210df.s3.amazonaws.com/90479255/289277800-f26513f7-cdf4-44ee-9a08-f6b27e6b99f7.jpg",
    title="AkenoX Beta AI API",
    version="1.0.0",
    summary="Use It Only For Personal Projects",
    description="Free API By akenoai-lib",
    routes=fast_app.routes,
)
```
### 🥷 Full-Stack Examples
- [X] Powerful & Super Fast Performance
- [X] Recommended RAM: 8GB / 16GB
- [X] Supports `bot_token` & `session_string`
- [X] Custom Web Frontend with HTML & CSS
```py
import logging
from akenoai import AkenoXToJs as js
from akenoai.runner import run_fast
from akenoai.clients import create_pyrogram

logger = logging.getLogger(__name__)
LOGS = logging.getLogger("[akenox]")
logger.setLevel(logging.DEBUG)

fast_app = js.get_app()
js.add_cors_middleware()

assistant = create_pyrogram(
    name="fastapi-bot",
    api_id=1234,
    api_hash="asdfghkl",
    bot_token="1235:asdfh"
)

user_client = create_pyrogram(
    name="fastapi-user",
    api_id=1234,
    api_hash="asdfghkl",
    session_string="session"
)

@fast_app.on_event("startup")
async def startup_event():
    bot = await assistant.start()
    user = await user_client.start()
    LOGS.info(f"Started UserBot & Assistant: {user.me.first_name} || {bot.me.first_name}")

@fast_app.get("/api/cohere")
async def cohere(query: str):
    return await js.randydev(
        "ai/cohere/command-plus",
        api_key="<your_api_key>",
        custom_dev_fast=True,
        query=query,
        chatHistory=[],
        system_prompt="You are a helpful AI assistant designed to provide clear and concise responses."
    )

@fast_app.get("/test")
async def example_json():
    async with js.fasthttp().ClientSession() as session:
        async with session.get("https://jsonplaceholder.typicode.com/todos/1") as response:
            title = js.dict_to_obj(await response.json()).title
    return {"message": title}

@fast_app.get("/api/tg/send_message")
async def send_message(text: str, chat_id: str):
    response_json = await client.send_message(chat_id, text)
    return {"message_id": response_json.id}

js.custom_openapi(
    app=fast_app,
    logo_url="https://github-production-user-asset-6210df.s3.amazonaws.com/90479255/289277800-f26513f7-cdf4-44ee-9a08-f6b27e6b99f7.jpg",
    title="AkenoX Beta AI API",
    version="1.0.0",
    summary="Use It Only For Personal Project",
    description="Free API By akenoai-lib",
    routes=fast_app.routes,
)

run_fast(build=fast_app)
```

- Use API Key V1 Free
```py
from akenoai import AkenoXToJs

response = await AkenoXToJs.randydev(
    "ai/openai/gpt-old",
     custom_dev_fast=True,
     query="hello world"
)
print(response)
```
<b>Output:</b>
```py
{'results': 'Deepseek is a Chinese company that specializes in underwater robotics and autonomous underwater vehicles. They provide solutions for underwater exploration and research, as well as services for inspecting and maintaining underwater infrastructure. Their technology is used in various industries including marine science, aquaculture, and offshore energy.\n\nPowered By xtdevs'}
```
### 🔹 <b>Method Definition:</b>

- [X] Parameters:
- `endpoint:` The API endpoint to call.
- `api_key:` (Optional) API key for authentication.
- `post:` Boolean flag to indicate POST requests.
- `is_obj:` Boolean flag indicating whether the response should be returned as a Python object (True) or in the default format (False).
- `custom_dev_fast:` Boolean flag defaults to None
- `**params:` Allows passing additional parameters as a dictionary, which will be sent as JSON.

```py
randydev(endpoint, api_key=None, post=False, is_obj=False, custom_dev_fast=False, **params)
```
### 🔹 <b>User Creation Date:</b>
```py
import os
from akenoai import AkenoXToJs

response = await AkenoXToJs.randydev(
    "user/creation-date",
    custom_dev_fast=True,
    user_id=client.me.id
)
return response
```
### 🔑 API Key
> [!NOTE]
> How to Get an API Key for AkenoX API?
>
> Different V1 Free and V2 Access Premium
>
> You can set up your API key using environment variables:
```env
AKENOX_KEY=akeno_xxxxxx
```
- To get an API key, [`@aknuserbot`](https://t.me/aknuserbot)

- 🚀 Thank you to our 2.7 million users per request!

### ⚠️ Problem Double Fix:
🛠️ **Double Fix for Connection Issues**
- ❌ **Cannot connect to host**
- 🚫 **IP address blocked issue**
- 🌐 **Different DNS settings**

### ❤️ Special Thanks To
- [`Kurigram`](https://github.com/KurimuzonAkuma/pyrogram)
- [`FastAPI`](https://github.com/fastapi/fastapi)

# Contributing
If you find a bug or have a feature request, please open an issue on our GitHub repository.

We welcome contributions from the community. If you'd like to contribute, please fork the repository and submit a pull request.

# License
[![License](https://www.gnu.org/graphics/agplv3-155x51.png)](LICENSE)
TeamKillerX is licensed under [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html) v3 or later.

<h4 align="center">Copyright (C) 2019 - 2025 The AkenoAI <a href="https://github.com/TeamKillerX">TeamKillerX</a>
<a href="https://t.me/xtdevs">@xtdevs</a>
</h4>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Project [akenoai-lib](https://github.com/TeamKillerX/) is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
