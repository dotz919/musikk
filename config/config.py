import os as _os
import re as _re
import sys as _sys

import dotenv as _dotenv
from pyrogram import filters as _flt

_dotenv.load_dotenv()

def is_bool(value: str) -> bool:
    return str(value).lower() in ["true", "yes"]

def parse_list(text: str, sep: str = ",") -> list[str]:
    if not text:
        text = ""
    return [v.strip() for v in str(text).strip("'\"").split(sep) if v.strip()]

def getenv(key, default=None):
    value = default
    if v := _os.getenv(key):
        value = v
    return value

# Get it from my.telegram.org
API_ID = int(getenv("API_ID", "20364494"))
API_HASH = getenv("API_HASH", "96a698baae5ff0d63ed642071eddbdae")

# Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "8390067122:AAE1fTIlTZJMBQjzkAi0ehfEajSIHzdhW_Q")

# Database to save your chats and stats... Get MongoDB
MONGO_DB_URI = getenv("MONGO_DB_URL", "mongodb+srv://dots123:dots123@cluster0.y7bjbmr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Your cookies pasted link on batbin.me
COOKIE_LINK = parse_list(getenv("COOKIE_LINK", ""))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "5"))

# Custom max audio(music) duration for voice chat
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "300"))

EXTRA_PLUGINS = is_bool(getenv("EXTRA_PLUGINS", "False"))

EXTRA_PLUGINS_REPO = getenv("EXTRA_PLUGINS_REPO", "https://github.com/TheTeamVivek/Extra-Plugin")

# Duration Limit for downloading Songs
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "90"))

# Group ID or username for log
LOG_GROUP_ID = getenv("LOG_GROUP_ID", "-1003441832323")

# Your User ID
OWNER_ID = list(map(int, getenv("OWNER_ID", "6739598575").split()))

# Heroku API
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

# Repository
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/hakutakaid/Music-Indo")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

# Git token (private repo)
GIT_TOKEN = getenv("GIT_TOKEN", "")

# Support
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/dotzstorereall")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/dotzsupoorrt")

# Auto leave assistant
AUTO_LEAVING_ASSISTANT = is_bool(getenv("AUTO_LEAVING_ASSISTANT", "False"))
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "5800"))

# Private bot
PRIVATE_BOT_MODE = is_bool(getenv("PRIVATE_BOT_MODE", "False"))

# Sleep downloader
YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "3"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "5"))

# Playlist & stream limit
VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "999"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "25"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))

# Telegram file size limit
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "1073741824"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))

# Auto set bot commands
SET_CMDS = is_bool(getenv("SET_CMDS", "False"))

# Pyrogram string session
STRING_SESSIONS = parse_list(getenv("STRING_SESSIONS", "BQE2vM4AI32Utk4k8YfYtlKZI2bAn3qbDLdyozUnSn0b_V73B7gZurjmQR6djkzVSqudyG0d8bRLicY3O8_ZgwO7BqxIMv5h44bPmuODR3Djkxacya4U5C0qKp3LJgTaRutwA2qozgLxc1mFkYTWrBTXCQVwdpbisc-DFUdJ6F0e2Nx785wkk0ZxSfy_wR5V1ZCtfQTny0wcJI6h1DlMVBplvIIhbXSIEAcsZ1YoEycKJGQCUxacxgnci3fngK9exXPbREZGyy-RL8KVcxRDxhoPYzP3s39jlyp61oV3HchYo3Z5dHMVtXAQezZGr4WQPa1W68ueJ9MbuwBJ09w_yvf3hRG-8gAAAAHO_CXMAA"))

# === DONT TOUCH CODE BELOW ===
BANNED_USERS = _flt.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []
