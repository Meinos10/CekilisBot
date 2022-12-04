from pyrogram import Client, filters, enums
from config import *
from pyrogram.types import Message
import os, asyncio, time
from cekilis.commands.buttons import katil
from cekilis.defs import *

@Client.on_message(filters.command("baslat"))
async def cekilis(client: Client, message: Message):
    if not message.from_user.id in sudo:
        return
    nereye = await client.ask(message.chat.id, "**Nerede çekiliş yapacağım lütfen bana oradan bir mesaj İLET!**")
    if not nereye.forward_from_chat:
        return await client.send_message(message.chat.id, "**Lütfen bir mesaj iletmeyi deneyin!\n\n/baslat**")
    konu = await client.ask(message.chat.id, "**Çekilişin konusunu yazın!**")
    if not konu.text:
        return await client.send_message(message.chat.id, "**Lütfen bir yazı formatında deneyin!\n\n/baslat**")
    sayi = await client.ask(message.chat.id, "**Kaç kişi kazanacak?**")
    if not sayi.text:
        return await client.send_message(message.chat.id, "**Lütfen sayıyı yazı olarak girin!**")
    try:
        s = int(sayi.text)
    except ValueError:
        return await client.send_message(message.chat.id, "**Lütfen sayıyı rakam olarak girin!**")
    bitis = await client.ask(message.chat.id, "**Lütfen bitiş tarihini girin!\n\nÖrnek: `27-11-2022 19:02`**")
    if not bitis.text:
        return await client.send_message(message.chat.id, "**Lütfen bir yazı formatında deneyin!\n\n/baslat**")
    
    if not nereye.forward_from_chat.id in os.listdir("./cekilis/database"):
        os.mkdir("./cekilis/database/"+str(nereye.forward_from_chat.id))
        open("./cekilis/database/"+str(nereye.forward_from_chat.id)+"/katılanlar.txt", "w", encoding="utf-8").write("")
        open("./cekilis/database/"+str(nereye.forward_from_chat.id)+"/konu.txt", "w", encoding="utf-8").write(str(konu.text))
        open("./cekilis/database/"+str(nereye.forward_from_chat.id)+"/sayi.txt", "w", encoding="utf-8").write(str(s))
        open("./cekilis/database/"+str(nereye.forward_from_chat.id)+"/bitis.txt", "w", encoding="utf-8").write(str(bitis.text))
    else:
        open("./cekilis/database/"+str(nereye.forward_from_chat.id)+"/katılanlar.txt", "w", encoding="utf-8").write("")
        open("./cekilis/database/"+str(nereye.forward_from_chat.id)+"/konu.txt", "w", encoding="utf-8").write(str(konu.text))
        open("./cekilis/database/"+str(nereye.forward_from_chat.id)+"/sayi.txt", "w", encoding="utf-8").write(str(s))
        open("./cekilis/database/"+str(nereye.forward_from_chat.id)+"/bitis.txt", "w", encoding="utf-8").write(str(bitis.text))

    msg = await client.send_message(nereye.forward_from_chat.id, f"**Çekiliş başladı!\n\n{konu.text} 🎉\n\nBitiş: `{bitis.text}`**", reply_markup=katil(message.from_user.id))
    await asyncio.sleep(2)
    await client.send_message(message.chat.id, "**Çekiliş başladı kontrol edebilirsin!**")
    await check(client, nereye.forward_from_chat.id, msg.id, message.from_user.id)

