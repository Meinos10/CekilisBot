from pyrogram import Client
from pyromod import listen
import os
from config import *

def sil():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

if "cekilis.session" in os.listdir():
    os.remove("cekilis.session")


Bot = Client(
    "cekilis",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=token,
    plugins=dict(root="cekilis.commands")
)


sil()
print("Bot çalışıyor!")
Bot.run()