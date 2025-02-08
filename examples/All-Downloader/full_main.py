# all downloader
import asyncio
import os
from akenoai import AkenoXToJs

api_key = os.environ.get("AKENOX_KEY")

async def TiktokDownloader(url: str):
    response = await AkenoXToJs.randydev(
        "dl/tiktok",
        api_key=api_key,
        custom_dev_fast=True,
        url=url
    )
    return response

async def FbDownloader(url: str):
    response = await AkenoXToJs.randydev(
        "dl/fb",
        api_key=api_key,
        custom_dev_fast=True,
        url=url
    )
    return response

# 100 max request per hour
async def TeraboxDownloader(url: str):
    response = await AkenoXToJs.randydev(
        "dl/terabox",
        api_key=api_key,
        custom_dev_fast=True,
        url=url
    )
    return response


async def main():
    teradl = await TeraboxDownloader("...")
    fbdl = await FbDownloader("...")
    ttk = await TiktokDownloader("...")
    print("terabox", teradl)
    print("fbdl", fbdl)
    print("tiktok", ttk)

if __name__ == "__main__":
    asyncio.run(main())

# You can use "dl/*" check output JSON
