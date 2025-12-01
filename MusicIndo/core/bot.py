import asyncio
import os
import sys
import traceback
from datetime import datetime
from functools import wraps

from pyrogram import Client, idle, StopPropagation
from pyrogram.enums import ChatMemberStatus
from pyrogram.handlers import MessageHandler
from pyrogram.types import (
    BotCommand,
    BotCommandScopeAllPrivateChats,
    BotCommandScopeAllGroupChats,
    BotCommandScopeAllChatAdministrators,
    BotCommandScopeChat,
    BotCommandScopeChatMember,
)

# ✅ HANYA IMPORT ERROR CLASS YANG BENAR DI VERSI TERBARU
from pyrogram.errors import RPCError
from pyrogram.errors.exceptions.forbidden_403 import Forbidden
from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import MessageIdInvalid, MessageNotModified

import config
from MusicIndo.logging import LOGGER


class Userbot(Client):
    def __init__(self):
        LOGGER(__name__).info("STARTING USERBOT...")

        super().__init__(
            name="UserBotMusicIndo",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=None,
            sleep_threshold=240,
            workers=50,
        )

    def on_message(self, filters=None, group=0):
        def decorator(func):
            @wraps(func)
            async def wrapper(client, message):
                try:
                    await func(client, message)

                # ✅ HANDLE FLOOD WAIT YANG BENAR
                except FloodWait as e:
                    LOGGER(__name__).warning(f"FLOOD WAIT {e.value}s, SLEEPING...")
                    await asyncio.sleep(e.value)

                # ✅ EXCEPT KOMPATIBEL, TIDAK ADA ERROR LAMA
                except (RPCError, Forbidden, BadRequest, MessageIdInvalid, MessageNotModified):
                    pass

                except StopPropagation:
                    raise

                except Exception as e:
                    err = traceback.format_exc()
                    LOGGER(__name__).error(err)
                    try:
                        await self.send_message(config.LOG_GROUP_ID, f"USERBOT ERROR:\n{err}")
                    except:
                        pass

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
        LOGGER(__name__).info(f"USERBOT STARTED AS {self.name}")

    async def stop(self):
        await super().stop()
        LOGGER(__name__).info("USERBOT STOPPED")
