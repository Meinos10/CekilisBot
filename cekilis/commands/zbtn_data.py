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
        if not str(user.id)+"%&/"+user.first_name in str(open("./cekilis/database/"+str(chat.id)+"/katılanlar.txt", "r", encoding="utf-8").read()).split("\n"):
            if str(open("./cekilis/database/"+str(chat.id)+"/katılanlar.txt", "r", encoding="utf-8").read()) == "":
                open("./cekilis/database/"+str(chat.id)+"/katılanlar.txt", "w", encoding="utf-8").write(str(user.id)+"%&/"+user.first_name+"\n")
            else:
                open("./cekilis/database/"+str(chat.id)+"/katılanlar.txt", "a", encoding="utf-8").write(str(user.id)+"%&/"+user.first_name+"\n")
            zaman = str(open("./cekilis/database/"+str(chat.id)+"/bitis.txt", "r", encoding="utf-8").read())
            tarih = str(zaman.split(" ")[0]).split("-")
            saat = str(zaman.split(" ")[1]).split(":")
            kalan = datetime.datetime(int(tarih[2]), int(tarih[1]), int(tarih[0]), int(saat[0]), int(saat[1])) - datetime.datetime.now()
            kisi = str(open("./cekilis/database/"+str(chat.id)+"/sayi.txt", "r", encoding="utf-8").read())
            konu = str(open("./cekilis/database/"+str(chat.id)+"/konu.txt", "r", encoding="utf-8").read())
            katılanlar = str(open("./cekilis/database/"+str(chat.id)+"/katılanlar.txt", "r", encoding="utf-8").read()).split("\n")
            if "" in katılanlar:
                katılanlar.remove("")
            if not kalan.seconds < 10:
                dakika = kalan.seconds // 60
                try:
                    await client.edit_message_text(
                        chat_id=chat.id,
                        message_id=callback.message.id,
                        text=f"**{konu} 🎉\n\nKazanacak kişi sayısı: `{kisi}`\n\nKalan süre: `{dakika}` dakika `{kalan.seconds - (dakika*60)}` saniye\n\nToplam katılımcı: `{len(katılanlar)}`**",
                        reply_markup=katil(user_id)
                    )
                except Exception as e:
                    print(e)
                    pass
            else:
                try:
                    await client.edit_message_text(
                        chat_id=chat.id,
                        message_id=callback.message.id,
                        text=f"**{konu} 🎉\n\nKazanacak kişi sayısı: `{kisi}`\n\nKalan süre: `{kalan.seconds}` saniye\n\nToplam katılımcı: `{len(katılanlar)}`**",
                        reply_markup=katil(user_id)
                    )
                except Exception as e:
                    print(e)
                    pass
        else:
            await callback.answer("Zaten çekilişe katıldınız!", show_alert=True)