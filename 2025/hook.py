from discord import SyncWebhook
import datetime
import time

url = "https://discord.com/api/webhooks/1448156600484233226/cmKy4xw1c6Qwt9uZDBeSHkGoBM8wH2YlnGrErsz-meQlsHDQgyUmA4kha_-cQRu-Bg-E"

while True:
    if datetime.datetime.today().hour == 22 and datetime.datetime.today().minute == 35 :
        webhook = SyncWebhook.from_url(url)
        webhook.send("someone ping nightly pings for me, im asleep lol")
        webhook.send("https://media.discordapp.net/attachments/962809053518635048/1448152261787386006/tenor_9.gif?ex=693a3864&is=6938e6e4&hm=ec7f8e437e06bd8ce9d153b7f2f7d05521ea6641ae9d250fb235a3073955d82a&=&width=1109&height=747")
        break
    else:
        print(datetime.datetime.today())
        time.sleep(60)