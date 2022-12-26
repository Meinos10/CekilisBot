import asyncio, random, datetime, os
from cekilis.commands.buttons import katil


async def check(client, chat_id, message_id, user_id):
    while True:
        zaman = str(open("./cekilis/database/"+str(chat_id)+"/bitis.txt", "r", encoding="utf-8").read())
        tarih = str(zaman.split(" ")[0]).split("-")
        saat = str(zaman.split(" ")[1]).split(":")
        kalan = datetime.datetime(int(tarih[2]), int(tarih[1]), int(tarih[0]), int(saat[0]), int(saat[1])) - datetime.datetime.now()
        kisi = str(open("./cekilis/database/"+str(chat_id)+"/sayi.txt", "r", encoding="utf-8").read())
        konu = str(open("./cekilis/database/"+str(chat_id)+"/konu.txt", "r", encoding="utf-8").read())
        katılanlar = str(open("./cekilis/database/"+str(chat_id)+"/katılanlar.txt", "r", encoding="utf-8").read()).split("\n")
        if "" in katılanlar:
            katılanlar.remove("")
        if not (kalan.seconds + 10800) < 10: # Sunucu saatindeki 3 saatlik arayı dengelemek için !
            dakika = (kalan.seconds + 10800) // 60
            try:
                await client.edit_message_text(
                    chat_id=chat_id,
                    message_id=message_id,
                    text=f"**{konu} 🎉\n\nKazanacak kişi sayısı: `{kisi}`\n\nKalan süre: `{dakika}` dakika `{(kalan.seconds + 10800) - (dakika*60)}` saniye\n\nToplam katılımcı: `{len(katılanlar)}`**",
                    reply_markup=katil(user_id)
                )
            except Exception as e:
                print(e)
                pass
        else:
            try:
                await client.edit_message_text(
                    chat_id=chat_id,
                    message_id=message_id,
                    text=f"**{konu} 🎉\n\nKazanacak kişi sayısı: `{kisi}`\n\nKalan süre: `{kalan.seconds + 10800}` saniye\n\nToplam katılımcı: `{len(katılanlar)}`**",
                    reply_markup=katil(user_id)
                )
            except Exception as e:
                print(e)
                pass
            await asyncio.sleep(kalan.seconds)
            katılanlar = str(open("./cekilis/database/"+str(chat_id)+"/katılanlar.txt", "r", encoding="utf-8").read()).split("\n")
            winner_users = ""
            n = 1
            for i in range(int(kisi)):
                try:
                    user = str(random.choice(katılanlar)).split("%&/")
                    katılanlar.remove(user[0]+"%&/"+user[1])
                    winner_users+=f"{n} - [{user[1]}](tg://user?id={user[0]})\n"
                    n+=1
                except Exception as e:
                    print(e)
                    pass
            try:
                await client.edit_message_text(
                    chat_id=chat_id,
                    message_id=message_id,
                    text=f"**{konu} 🎉\n\n`Süre Bitti!`\n\nKazananlar;\n\n{winner_users}\nToplam katılımcı: `{len(katılanlar)}`**"
                )
            except Exception as e:
                print(e)
                pass
            try:
                for i in os.listdir("./cekilis/database/"+str(chat_id)):
                    os.remove("./cekilis/database/"+str(chat_id)+"/"+i)
                os.rmdir("./cekilis/database/"+str(chat_id))
            except:
                pass
            return




        
        await asyncio.sleep(5)
