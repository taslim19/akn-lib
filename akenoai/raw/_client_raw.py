# created by @xtdevs

from pyrogram import Client
from pyrogram.raw import functions

class RawFunctions:
    def __init__(self, class_client=Client):
        self.client = class_client
        self.functions_ = functions

    async def reactions(self, peers=None, results_updates: bool = False):
        results = await self.client.invoke(
            self.functions_.messages.ReadReactions(
                peer=await self.client.resolve_peer(peers)
            )
        )
        if results_updates:
            return results

    async def mention_and_tags(self, peers=None, results_updates: bool = False):
        results = await self.client.invoke(
            self.functions_.messages.ReadMentions(
                peer=await self.client.resolve_peer(peers)
            )
        )
        if results_updates:
            return results

    async def send_screenshot_notification(self, peers=None, results_updates: bool = False):
        results = await self.client.invoke(
            await self.functions_.messages.SendScreenshotNotification(
                peer=await self.client.resolve_peer(peers),
                reply_to_msg_id=0,
                random_id=self.client.rnd_id()
            )
        )
        if results_updates:
            return results
