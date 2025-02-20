#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Credits @xpushz on telegram
# Copyright 2020-2025 (c) Randy W @xtdevs, @xtsea on telegram
#
# from : https://github.com/TeamKillerX
# Channel : @RendyProjects
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import asyncio
import json
import os
import subprocess
from base64 import b64decode as m
from datetime import datetime

import aiohttp
import httpx
import requests
import uvloop
import wget
from box import Box

import akenoai.logger as fast


class BaseDev:
    def __init__(self, public_url: str):
        self.public_url = public_url
        self.obj = Box

    def _prepare_request(self, endpoint: str, api_key: str = None, headers_extra: dict = None):
        """Prepare request URL and headers."""
        if not api_key:
            api_key = os.environ.get("AKENOX_KEY")
        if not api_key:
            raise ValueError("Required variables AKENOX_KEY or api_key")
        url = f"{self.public_url}/{endpoint}"
        headers = {
            "x-api-key": api_key,
            "Authorization": f"Bearer {api_key}"
        }
        if headers_extra:
            headers.update(headers_extra)
        return url, headers

    async def _make_request(self, method: str, endpoint: str, **params):
        """Handles async API requests."""
        url, headers = self._prepare_request(endpoint, params.pop("api_key", None))
        try:
            async with aiohttp.ClientSession() as session:
                request = getattr(session, method)
                async with request(url, headers=headers, params=params) as response:
                    return await response.json()
        except (aiohttp.client_exceptions.ContentTypeError, json.decoder.JSONDecodeError):
            raise Exception("GET OR POST INVALID: check problem, invalid JSON")
        except (aiohttp.ClientConnectorError, aiohttp.client_exceptions.ClientConnectorSSLError):
            raise Exception("Cannot connect to host")
        except Exception:
            return None

class RandyDev(BaseDev):
    def __init__(self, public_url: str = "https://randydev-ryu-js.hf.space/api/v1"):
        super().__init__(public_url)
        self.chat = self.Chat(self)
        self.downloader = self.Downloader(self)

    class Chat:
        def __init__(self, parent: BaseDev):
            self.parent = parent

        async def create(self, model: str = None, is_obj=False, **kwargs):
            """Handle AI Chat API requests."""
            if not model:
                raise ValueError("Model name is required for AI requests.")
            response = await self.parent._make_request("get", f"ai/{model}", **kwargs) or {}
            return self.parent.obj(response) if is_obj else response

    class Downloader:
        def __init__(self, parent: BaseDev):
            self.parent = parent

        @fast.log_performance
        async def create(self, model: str = None, is_obj=False, **kwargs):
            """Handle downloader API requests."""
            if not model:
                raise ValueError("Model name is required for downloader requests.")
            response = await self.parent._make_request("get", f"dl/{model}", **kwargs) or {}
            return self.parent.obj(response) if is_obj else response

class AkenoXJs:
    def __init__(self, public_url: str = "https://randydev-ryu-js.hf.space/api/v1"):
        self.randydev = RandyDev(public_url)

AkenoXToJs = AkenoXJs
