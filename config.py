# +++ Modified By [telegram username: @BotifyX_Pro_Botz
import os
from os import environ
import logging
from logging.handlers import RotatingFileHandler

# Recommended
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8470581615:AAG3P6SMKb60oLgdzn1HPUJZm4BAiKBWJ30")
APP_ID = int(os.environ.get("APP_ID", "27226524"))
API_HASH = os.environ.get("API_HASH", "a14c9cd4629fde6b4d9b8c77df00fb00")

# Main
OWNER_ID = int(os.environ.get("OWNER_ID", "7156099919"))
PORT = os.environ.get("PORT", "8050")

# Database
DB_URI = os.environ.get("DB_URI", "mongodb+srv://ANI_OTAKU:ANI_OTAKU@cluster0.t3frstc.mongodb.net/?appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "linksharebot")

#Auto approve 
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '').split()] # dont change anything 
TEXT = environ.get("APPROVED_WELCOME_TEXT", "<b>{mention},\n\nʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ {title} ɪs ᴀᴘᴘʀᴏᴠᴇᴅ.\n\‣ ᴘᴏᴡᴇʀᴇᴅ ʙʏ @BotifyX_Pro_Botz</b>")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

# Default
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -

# Start pic
START_PIC = "https://ibb.co/xttfrkw9"
START_IMG = "https://ibb.co/ds3yDQ4B"
# Messages
START_MSG = os.environ.get("START_MESSAGE", "<b>ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴀᴅᴠᴀɴᴄᴇᴅ ʟɪɴᴋs sʜᴀʀɪɴɢ ʙᴏᴛ. ᴡɪᴛʜ ᴛʜɪs ʙᴏᴛ, ʏᴏᴜ ᴄᴀɴ sʜᴀʀᴇ ʟɪɴᴋs ᴀɴᴅ ᴋᴇᴇᴘ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟs sᴀғᴇ ғʀᴏᴍ ᴄᴏᴘʏʀɪɢʜᴛ ɪssᴜᴇs.\n\n<blockquote>‣ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://t.me/BotifyX_Pro_Botz'>彡 ΔNI_OTΔKU 彡</a></blockquote></b>")
HELP = os.environ.get("HELP_MESSAGE", "<b><blockquote expandable>» Creator: <a href=https://t.me/@ITS_shun_x>ₛₕᵤₙ</a>\n» Our Community: <a href=https://t.me/ANIME_X_FLEX>ᴏᴛᴀᴋᴜғʟɪx</a>\n» Anime Channel: <a href=https://t.me/Anime_z_Flex>ᴀɴɪᴍᴇ_ғʟɪx</a>\n» Ongoing Anime: <a href=https://t.me/Anime_z_Flex>ᴀɴɪᴍᴇ_ғʟɪx</a>\n» Developer: <a href=https://t.me/ITS_shun_x>ₛₕᵤₙ</a></b>")
ABOUT = os.environ.get("ABOUT_MESSAGE", "<b><blockquote expandable>This bot is developed by ₛₕᵤₙ (@ITS_shun_x) to securely share Telegram channel links with temporary invite links, protecting your channels from copyright issues.</b>")

ABOUT_TXT = """<b>›› ᴄᴏᴍᴍᴜɴɪᴛʏ: <a href='https://t.me/ANIME_X_FLEX'>ᴏᴛᴀᴋᴜғʟɪx</a>
<blockquote expandable>›› ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/BotifyX_Pro_Botz'>Cʟɪᴄᴋ ʜᴇʀᴇ</a>
›› ᴏᴡɴᴇʀ: <a href='https://t.me/ITSANIMEN'>彡 ΔNI_OTΔKU 彡</a>
›› ʟᴀɴɢᴜᴀɢᴇ: <a href='https://docs.python.org/3/'>Pʏᴛʜᴏɴ 3</a>
›› ʟɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ ᴠ2</a>
›› ᴅᴀᴛᴀʙᴀsᴇ: <a href='https://www.mongodb.com/docs/'>Mᴏɴɢᴏ ᴅʙ</a>
›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: @ITS_shun_x</b></blockquote>""" # Bhosdiwalo agar developer me Yato ka username hataya to agli baar se koi repo public nhi krunga!!

CHANNELS_TXT = """<b>›› ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/Anime_z_Flex'>ᴀɴɪᴍᴇ_ғʟɪx</a>
<blockquote expandable>›› ᴀɴɪᴍᴇ ᴍᴏᴠɪᴇs: <a href='https://t.me/OTAKU_Mania'>ᴀɴɪ_ᴍᴏᴠɪᴇ's</a>
›› ᴀɴɪᴍᴇ ᴇᴅɪᴛ: <a href='https://t.me/Animez_Edits'>ᴀɴɪᴍᴇ'ᴢ ᴇᴅɪᴛ'ᴢ</a>
›› ᴍᴀɴʜᴡᴀ ᴄʜᴀɴɴᴇʟs: <a href='https://t.me/+Yr5A0bOSR0I4NGU1'>ᴍᴀɴɢᴀ_ᴅᴇᴠɪʟ</a>
›› ᴘᴏʀɴʜᴡᴀ ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/pornwhaa_flix'>ᴘᴏʀɴʜᴡᴀ_ғʟɪx</a>
›› ᴄᴏᴍᴍᴜɴɪᴛʏ: <a href='https://t.me/ANIME_X_FLEX'>ᴏᴛᴀᴋᴜғʟɪx</a>
›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: @ITS_shun_x</b></blockquote>""" # Bhosdiwalo agar developer me Yato ka username hataya to agli baar se koi repo public nhi krunga!!

#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -
# Default
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "⚠️ ғᴜᴄᴋ ʏᴏᴜ, ɢᴏ ᴀᴡᴀʏ ʙɪᴛᴄʜ!"

# Logging
LOG_FILE_NAME = "links-sharingbot.txt"
DATABASE_CHANNEL = int(os.environ.get("DATABASE_CHANNEL", "-1003548938800")) # Channel where user links are stored
#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -

try:
    ADMINS = []
    for x in (os.environ.get("ADMINS", "7156099919").split()):
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

# Admin == OWNER_ID
ADMINS.append(OWNER_ID)
ADMINS.append(7156099919)


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
