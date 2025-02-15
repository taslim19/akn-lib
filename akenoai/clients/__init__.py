from pyrogram import Client


def create_pyrogram(name: str, **args):
    return Client(name, **args)
