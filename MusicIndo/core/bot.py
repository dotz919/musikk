import asyncio
import importlib.util
import os
import traceback
from datetime import datetime
from functools import wraps

from pyrogram import Client
from pyrogram.enums import ChatMemberStatus
from pyrogram.handlers import MessageHandler

from pyrogram.errors import RPCError
from pyrogram.errors.exceptions.forbidden_403 import Forbidden
from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import MessageIdInvalid, MessageNotModified

import config
from MusicIndo.logging import LOGGER

# ✅ IMPORT USERBOT SUDAH FIXED
from MusicIndo.core.userbot import Userbot

class YukkiBot(Client):
    def __init__(self):
        LOGGER(__name__).info("STARTING BOT...")

        super().__init__(
            name="MusicIndo",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            sleep_threshold=240,
            workers=50,
        )
        self.loaded_plug_counts = 0

    def on_message(self, filters=None, group=0):
        def decorator(func):
            @wraps(func)
            async def wrapper(client, message):
                try:
                    await func(client, message)
                except FloodWait as e:
                    await asyncio.sleep(e.value)
                except (RPCError, Forbidden, FloodWait, MessageIdInvalid, MessageNotModified):
                    pass
                except Exception:
                    LOGGER(__name__).error(traceback.format_exc())
            self.add_handler(MessageHandler(wrapper, filters), group)
            return func
        return decorator

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.username = me.username
        self.id = me.id
        self.name = me.full_name
        self.mention = me.mention

        LOGGER(__name__).info(f"BOT STARTED AS {self.name}")
        try:
            await self.send_message(config.LOG_GROUP_ID, f"{self.mention} BOT STARTED")
        except Exception:
            pass

# ✅ INITIALIZER INSTANCE
app = YukkiBot()
userbot = Userbot()
HELPABLE = {}
