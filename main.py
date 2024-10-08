import os
from pyrogram import Client as AFK, idle
from pyrogram.enums import ChatMemberStatus, ChatMembersFilter
from pyrogram import enums
from pyrogram.types import ChatMember
import asyncio
import logging
import tgcrypto
from pyromod import listen
import logging
from tglogging import TelegramLogHandler

# Config 
class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7527732730:AAHnepoD_bJmwU9K6sCFO1sen3XQp9GZmPQ")
    API_ID = int(os.environ.get("API_ID",  "23865844"))
    API_HASH = os.environ.get("API_HASH", "644ca71d8f3a8bf718cc317c53114d9d")
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    SESSIONS = "./SESSIONS"

    AUTH_USERS = os.environ.get('AUTH_USERS', '6622333718').split(',')
    for i in range(len(AUTH_USERS)):
        AUTH_USERS[i] = int(AUTH_USERS[i])

    GROUPS = os.environ.get('GROUPS', '-4531533177').split(',')
    for i in range(len(GROUPS)):
        GROUPS[i] = int(GROUPS[i])

    LOG_CH = os.environ.get("LOG_CH", "-1002159628443")

# TelegramLogHandler is a custom handler which is inherited from an existing handler. ie, StreamHandler.
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        TelegramLogHandler(
            token=Config.BOT_TOKEN, 
            log_chat_id= Config.LOG_CH, 
            update_interval=2, 
            minimum_lines=1, 
            pending_logs=200000),
        logging.StreamHandler()
    ]
)

LOGGER = logging.getLogger(__name__)
LOGGER.info("live log streaming to telegram.")


# Store
class Store(object):
    CPTOKEN = "eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6MzI3OTI5MjcsIm9yZ0lkIjo2MjMxOSwidHlwZSI6MSwibW9iaWxlIjoiOTE4MzIwNzkzNTUzIiwibmFtZSI6IkhBUlNBIEpBTkdJRCBCQVJNRVIiLCJlbWFpbCI6ImhhcmlzaHBkaGVlckBnbWFpbC5jb20iLCJpc0ludGVybmF0aW9uYWwiOjAsImRlZmF1bHRMYW5ndWFnZSI6IkVOIiwiY291bnRyeUNvZGUiOiJJTiIsImNvdW50cnlJU08iOiI5MSIsInRpbWV6b25lIjoiR01UKzU6MzAiLCJpc0RpeSI6dHJ1ZSwib3JnQ29kZSI6ImFmYWtvIiwiaXNEaXlTdWJhZG1pbiI6MCwiZmluZ2VycHJpbnRJZCI6IjJiMzAxYzM0Yjg5MWZiYTJhNWNmMmI2MjQwNzY1YTQyIiwiaWF0IjoxNzI0MjI0MjExLCJleHAiOjE3MjQ4MjkwMTF9.oBcdII5Eq-aHNKspGrmp-2M5-Tu5DLcEWp5bgGhEqRnCf-zrniKu7D_JqBellQIm"
    SPROUT_URL = "https://discuss.oliveboard.in/"
    ADDA_TOKEN = ""
    THUMB_URL = "https://telegra.ph/file/84870d6d89b893e59c5f0.jpg"

# Format
class Msg(object):
    START_MSG = "**/pro**"

    TXT_MSG = "Hey <b>{user},"\
        "\n\n`I'm Multi-Talented Robot. I Can Download Many Type of Links.`"\
            "\n\nSend a TXT or HTML file :-</b>"

    ERROR_MSG = "<b>DL Failed ({no_of_files}) :-</b> "\
        "\n\n<b>Name: </b>{file_name},\n<b>Link:</b> `{file_link}`\n\n<b>Error:</b> {error}"

    SHOW_MSG = "<b>Downloading :- "\
        "\n**🎞️ Title :** `{file_name}`\n\nLink :- `{file_link}`</b>"

    CMD_MSG_1 = "`{txt}`\n\n**Total Links in File are :-** {no_of_links}\n\n**Send any Index From `[ 1 - {no_of_links} ]` :-**"
    CMD_MSG_2 = "<b>📤 𝐔𝐏𝐋𝐎𝐀𝐃𝐈𝐍𝐆! 📤</b> 🎞️ Title : `{file_name}`"
    RESTART_MSG = "✅ HI Bhai log\n✅ PATH CLEARED"

# Prefixes
prefixes = ["/", "~", "?", "!", "."]

# Client
plugins = dict(root="plugins")
if __name__ == "__main__":
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    if not os.path.isdir(Config.SESSIONS):
        os.makedirs(Config.SESSIONS)

    PRO = AFK(
        "AFK-DL",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        sleep_threshold=120,
        plugins=plugins,
        workdir= f"{Config.SESSIONS}/",
        workers= 2,
    )

    chat_id = []
    for i, j in zip(Config.GROUPS, Config.AUTH_USERS):
        chat_id.append(i)
        chat_id.append(j)
    
    
    async def main():
        await PRO.start()
        # h = await PRO.get_chat_member(chat_id= int(-1002115046888), user_id=6695586027)
        # print(h)
        bot_info = await PRO.get_me()
        LOGGER.info(f"<--- @{bot_info.username} Started --->")
        
        for i in chat_id:
            try:
                await PRO.send_message(chat_id=i, text="**Bot Started! ♾ /pro **")
            except Exception as d:
                print(d)
                continue
        await idle()

    asyncio.get_event_loop().run_until_complete(main())
    LOGGER.info(f"<---Bot Stopped--->")
