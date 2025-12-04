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
BOT_TOKEN = getenv("BOT_TOKEN", "8390067122:AAFFy_m-CBON0NlvaJpSQZRsLO6Gj1CLGMI")

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
    "BQE2vM4AUZHTD0TIdV599K3E4oO1z3lNahI0tfGAZ4FBC1WjDsUwRacc7CABAoKNctxhNYuBVg75hnE5Saoyry9Znsvv9GeXpf-eoSQBEnUVcc9M8FrqOISOwb90OAGCIghC0MHDsMb26482TMAei2MVq-AFFS8ckROa8wVpfJF8qWlGvtwp0L0mdBZ3pW1qbsE9Oa2YEE1KGAMnGJHtg1YAFiaSdLclqSxzoSB188T_cWzzC14rXgSLFBoY03aUuOHtDkR0UC3KRmaV5PttkDtMzRsUU9cpjI0EbA170qwTwDb84E0LRdE4-lr8z7aRZzyJ1N_TrU5O5irX_Nsx9zRGZhQhoQAAAAHO_CXMAA"
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
