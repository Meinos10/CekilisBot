from pyrogram import Client, filters, enums
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
import os, datetime
from cekilis.commands.buttons import katil

@Client.on_callback_query()
async def _(client: Client, callback: CallbackQuery):
    btn_data, user_id = callback.data.split()

    user = callback.from_user
    chat = callback.message.chat

    if btn_data == "katil":
        users = []
        for i in str(open("./cekilis/database/"+str(chat.id)+"/katılanlar.txt", "r", encoding="utf-8").read()).split("\n"):
            if not i == "":
                if not int(i.split("%&/")[0]) in users:
                    users.append(int(i.split("%&/")[0]))
        if not user.id in users:
            if str(open("./cekilis/database/"+str(chat.id)+"/katılanlar.txt", "r", encoding="utf-8").read()) == "":
                open("./cekilis/database/"+str(chat.id)+"/katılanlar.txt", "w", encoding="utf-8").write(str(user.id)+"%&/"+user.first_name+"\n")
            else:
                open("./cekilis/database/"+str(chat.id)+"/katılanlar.txt", "a", encoding="utf-8").write(str(user.id)+"%&/"+user.first_name+"\n")
        else:
            await callback.answer("Zaten çekilişe katıldınız!", show_alert=True)
