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
SESSION = "AQC2dpwTh7AfSfSn6A9iUt_-gWv8uKdDHY4F3rohS5fMyZZS39SrtjwTzF2vm_R4933NESyYa2F5RrneILqTwt7TRiIMrrrkLZ6XkBu_jnNXp1t2JCchvnoIbP604lTU8B0s5bilH7xcT5N8vzW-hTPnop6VSoI3FM4DTF0fKj3BOQbRGmgo48medNPtQ7mSikD2B6dQaNgIXwA4em0GyHDq7iQeGkiyN9jk8NKKcIpbTsiMxFdH2hTzBNpkHBWBjVSnxX61y9T7MXpc9q0u8QAZIgjpvECDrtZbzoDd3UuXqQtlwcLh8hk6nf6HjkG-oRlmKQhngp_IdvCJGvrWcYEgKUrOxgA"("SESSION", default=None)
FORCESUB = "hbvvfj"("FORCESUB", default=None)
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
