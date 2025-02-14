import os
import re

import setuptools


def read(fname, version=False):
    text = open(os.path.join(os.path.dirname(__file__), fname), encoding="utf8").read()
    if version:
        return re.search(r'__version__ = "(.*?)"', text).group(1)
    return text


setuptools.setup(
    name="akenoai",
    packages=setuptools.find_packages(),
    version=read("akenoai/__version__.py", version=True),
    license="MIT",
    description="AkenoAi Python Wrapper For Plus+",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="TeamKillerX",
    project_urls={
        "Source": "https://github.com/TeamKillerX/akenoai-lib/",
        "Issues": "https://github.com/TeamKillerX/akenoai-lib/issues",
    },
    keywords=[
        "API",
        "akeno-lib",
    ],
    install_requires=[
        "requests",
    ],
    extras_require={
        "fast": [
            "aiohttp",
            "wget",
            "requests",
            "httpx[http2]",
            "python-box",
            "starlette",
            "uvicorn[standard]",
            "fastapi[all]",
            "kurigram",
            "TgCrypto",
            "streamlit-option-menu",
            "streamlit-nightly",
        ],
        "standard": [
            "g4f",
            "httpx[http2]",
            "typing",
            "aiohttp",
            "bs4",
            "openai",
            "google-generativeai",
            "curl_cffi",
            "motor",
            "typing-extensions",
            "huggingface-hub>=0.23.2",
            "authlib",
            "gpytranslate",
            "fastapi[all]",
            "uvicorn[standard]",
            "kurigram",
        ],
        "all": [
            "aiohttp",
            "aiofiles",
            "kurigram",
            "bs4",
            "google-search-results",
            "httpx[http2]",
            "Python-IO",
            "Pillow",
            "openai",
            "tqdm",
            "pre-commit",
            "gpytranslate",
            "Flask",
            "pymongo",
            "pytz",
            "urllib3",
            "pydantic",
            "typing-extensions",
            "typing",
            "deprecation",
            "psutil",
            "screeninfo",
            "g4f",
            "curl_cffi",
            "google-generativeai",
            "gradio-client",
            "gradio",
            "huggingface-hub>=0.23.2",
            "motor",
            "wget",
            "uvicorn[standard]",
            "fastapi[all]",
            "authlib",
            "numpy",
            "python-dateutil",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Natural Language :: English",
    ],
    python_requires="~=3.7",
)
