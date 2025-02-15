from pyrogram import Client
from akenoai.clients.enums import EnumsDev as EnumsDev

def create_pyrogram(name: str, **args):
    return Client(name, **args)
