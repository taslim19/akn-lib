# akenoai-lib
🔹 <b>Recommended Installation:</b>

✅ Install via [`PYPI`](https://pypi.org/project/akenoai) for the latest updates. eg: `pip3 install akenoai[fast]`

<b>endpoints like:</b>
  - `ai/gpt-old`: query
  - `ai/copilot2-trip`: q
  - `anime/hentai`: None
  - `dl/fb`: url
  - `dl/xnxx`: url
  - Supports <b>custom parameters</b> for flexibility.

> [!TIP]
> Trip PRO Usage Example:
```py
from akenoai import AkenoXToJs

response = await AkenoXToJs.randydev("ai/gpt-old", allow_same=True, query="hello world")
print(response)
```
<b>Output:</b>
```py
{'results': 'Deepseek is a Chinese company that specializes in underwater robotics and autonomous underwater vehicles. They provide solutions for underwater exploration and research, as well as services for inspecting and maintaining underwater infrastructure. Their technology is used in various industries including marine science, aquaculture, and offshore energy.\n\nPowered By xtdevs'}
```
🔹 <b>Method Definition:</b>
```py
randydev(endpoint, api_key=None, post=False, allow_same=False, custom_dev=False, **params)
```
> [!NOTE]
> How to Get an API Key for AkenoX API?
>
> You can set up your API key using environment variables:
```env
AKENOX_NAME=randydev-ryu-js
AKENOX_KEY=akeno_xxxxxx
```
- To get an API key, [`@aknuserbot`](https://t.me/aknuserbot)

- 🚀 Thank you to our 2.7 million users per request!

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
