#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 28454303("API_ID", default=None, cast=int)
API_HASH = "69f36b96f0d1abab85adae3bd5108bf2"("API_HASH", default=None)
BOT_TOKEN = "6162530663:AAFNS9i2IDxQ5PdPNm6FkIcTStU39KXCwgg"("BOT_TOKEN", default=None)
SESSION = "AQCuUv-FgR4HIlrNnFsimjYAP0SID6o0kOcnO61f5CdenYjq0FNe-juulEuXkZ-inLzWkKdVa9LQZ0MkiVXkDrscPBTcrt5A5gfzvvJJEuFohueyyblGi64YC6aTPuvR96dfmabdInpPq0akkhW4sOUDJe-idOFIm70W0inZDCmg9LjxbkNigd7fcZ4CuHROtg2oPgntqO7ws_9qMUr58U6UERDf7sAgb75cW7LTOf3nuN0dOoHVNlYkS5xygyI83KIWuCaHkE_ck4HrbUSemPgUzcq-esNOFFhxbTyJuEMQagmgTBldNDcTJc0rCAFbSHM6GqmyYhciPaKVEFzs_5BkKUrOxgA"("SESSION", default=None)
FORCESUB = "djecgsx"("FORCESUB", default=None)
AUTH = 692768454("AUTH", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
