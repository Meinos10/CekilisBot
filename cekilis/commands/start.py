from pyrogram import Client, filters, enums
from config import *
from pyrogram.types import Message
import os, asyncio

@Client.on_message(filters.command("start"))
async def start(client: Client, message: Message):
    if not message.from_user.id in sudo:
        return
    await client.send_message(message.chat.id, "**Bot çalışıyor!**")
    