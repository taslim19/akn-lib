import asyncio
import json
import os
import subprocess
from datetime import datetime

import aiohttp
import requests
import streamlit
from box import Box
from streamlit_option_menu import option_menu

import akenoai.logger as fast


class StreamlitJs:
    def __init__(self):
        self.public_url = "https://randydev-ryu-js.hf.space"
        self.obj = Box
        self.request_in = aiohttp
        self.st = streamlit

    def stl(self):
        return self.st

    def set_page_config(self, **args):
        self.st.set_page_config(**args)

    def app_option_menu(self, **args):
        return option_menu(**args)

    def hide_streamlit_watermark(self, unsafe_allow_html=True):
        hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .css-1rs6os {visibility: hidden;}
        .css-17ziqus {visibility: hidden;}
        </style>
        """
        self.st.markdown(hide_streamlit_style, unsafe_allow_html=unsafe_allow_html)
        self.st.header("")

    def dict_to_obj(self, func):
        return self.obj(func or {})

    def _prepare_request(self, endpoint, api_key=None):
        """Prepare common request parameters and validate API key."""
        if not api_key:
            api_key = os.environ.get("AKENOX_KEY")
        if not api_key:
            raise ValueError("Required variables AKENOX_KEY or api_key")
        url = f"{self.public_url}/api/v1/{endpoint}"
        headers = {"x-api-key": api_key}
        return url, headers

    def _make_request_in(self, endpoint, api_key=None, post=False, verify=False, **params):
        url, headers = self._prepare_request(endpoint, api_key)
        try:
            if post:
                response = requests.post(url, headers=headers, params=params, verify=verify)
                return response.json() if endpoint != "maker/carbon" else response.content
            else:
                response = requests.get(url, headers=headers, params=params, verify=verify)
                return response.json() if endpoint != "maker/carbon" else response.content
        except json.decoder.JSONDecodeError:
            raise Exception("GET OR POST INVALID: check problem, invalid json")
        except requests.exceptions.ConnectionError:
            raise Exception("Cannot connect to host")
        except Exception as e:
            return str(e)

    @fast.no_async_log_performance
    def no_async_randydev(
        self,
        endpoint,
        api_key=None,
        post=False,
        is_obj=False,
        verify=True,
        **params
    ):
        if is_obj:
            return Box(self._make_request_in(endpoint, api_key, post=post, verify=verify, **params) or {})
        else:
            return self._make_request_in(endpoint, api_key, post=post, verify=verify, **params)

StreamlitToJs = StreamlitJs()
