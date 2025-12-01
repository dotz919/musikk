import os as _os
import sys as _sys
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

def is_bool(value: str) -> bool:
    return str(value).lower() in ["true", "yes", "1"]

def parse_list(text: str, sep: str = ",") -> list[str]:
    if not text:
        text = ""
    return [v.strip() for v in str(text).strip("'\"").split(sep) if v.strip()]

def getenv(key, default=None):
    if (v := _os.getenv(key)) is not None:
        return v
    return default

# Telegram API (USERBOT/ASSISTANT LOGIN)
API_ID = int(getenv("API_ID", "20364494"))
API_HASH = getenv("API_HASH", "96a698baae5ff0d63ed642071eddbdae")

# Bot token dari BotFather
BOT_TOKEN = getenv("BOT_TOKEN", "8390067122:AAE1fTIlTZJMBQjzkAi0ehfEajSIHzdhW_Q")

# MongoDB database URI
MONGO_DB_URI = getenv(
    "MONGO_DB_URI",
    "mongodb+srv://dots123:dots123@cluster0.y7bjbmr.mongodb.net/MusicIndo?retryWrites=true&w=majority"
)

# Owner bot (ADMIN CONTROL)
OWNER_ID = list(map(int, getenv("OWNER_ID", "6739598575").split(",")))

# Assistant login pakai STRING SESSION, BUKAN phone number
STRING_SESSION = getenv(
    "STRING_SESSION",
    "BQE2vM4AI32Utk4k8YfYtlKZI2bAn3qbDLdyozUnSn0b_V73B7gZurjmQR6djkzVSqudyG0d8bRLicY3O8_ZgwO7BqxIMv5h44bPmuODR3Djkxacya4U5C0qKp3LJgTaRutwA2qozgLxc1mFkYTWrBTXCQVwdpbisc-DFUdJ6F0e2Nx785wkk0ZxSfy_wR5V1ZCtfQTny0wcJI6h1DlMVBplvIIhbXSIEAcsZ1YoEycKJGQCUxacxgnci3fngK9exXPbREZGyy-RL8KVcxRDxhoPYzP3s39jlyp61oV3HchYo3Z5dHMVtXAQezZGr4WQPa1W68ueJ9MbuwBJ09w_yvf3hRG-8gAAAAHO_CXMAA"
)

# Group log ID (WAJIB INTEGER)
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1003441832323"))

# Batas durasi music/streaming
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "300"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "90"))

# Plugin extra opsional
EXTRA_PLUGINS = is_bool(getenv("EXTRA_PLUGINS", "False"))
EXTRA_PLUGINS_REPO = getenv("EXTRA_PLUGINS_REPO", "")

# Mode private bot
PRIVATE_BOT_MODE = is_bool(getenv("PRIVATE_BOT_MODE", "False"))

# File limit Telegram
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "1073741824"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))

# Auto leave assistant
AUTO_LEAVING_ASSISTANT = is_bool(getenv("AUTO_LEAVING_ASSISTANT", "False"))
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "5800"))

# Auto set command bot
SET_CMDS = is_bool(getenv("SET_CMDS", "False"))

# Filter banned user
BANNED_USERS = filters.user()

# Storage variable
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []
assistants = []
autoclean_list = []
