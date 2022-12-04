from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def katil(user_id):
    BUTTON = [[InlineKeyboardButton("Çekilişe Katıl!", callback_data=" ".join(["katil", str(user_id)]))]]
    return InlineKeyboardMarkup(BUTTON)