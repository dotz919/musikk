import asyncio
import sys
import traceback
from datetime import datetime
from functools import wraps

from pyrogram import Client, StopPropagation
from pyrogram.errors import ChatAdminRequired, ChatWriteForbidden, FloodWait, MessageIdInvalid, MessageNotModified
from pyrogram.handlers import MessageHandler

import config
from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot:
    def __init__(self):
        self.clients = [
            Client(
                f"MusicIndoString_{i}",
                api_id=config.API_ID,
                api_hash=config.API_HASH,
                session_string=session.strip(),
            )
            for i, session in enumerate(config.STRING_SESSIONS, start=1)
        ]
        self.handlers = []

    async def _start(self, client, index):
        LOGGER(__name__).info(f"STARTING ASSISTANT CLIENT {index}")
        try:
            await client.start()
            assistants.append(index)

            # Coba kirim log
            try:
                await client.send_message(config.LOG_GROUP_ID, "ASSISTANT STARTED")
            except ChatWriteForbidden:
                try:
                    await client.join_chat(config.LOG_GROUP_ID)
                    await client.send_message(config.LOG_GROUP_ID, "ASSISTANT STARTED")
                except Exception:
                    LOGGER(__name__).error(
                        f"ASSISTANT {index} GAGAL MENGIRIM LOG. TAMBAHKAN KE GROUP LOG!"
                    )
                    sys.exit(1)

            me = await client.get_me()
            client.id = me.id
            client.name = f"{me.first_name} {me.last_name or ''}".strip()
            client.username = me.username
            client.mention = me.mention
            assistantids.append(me.id)

            # Tambahkan handler yang sudah tersimpan
            for handler, group in self.handlers:
                client.add_handler(handler, group)

        except Exception as e:
            LOGGER(__name__).error(
                f"ASSISTANT {index} GAGAL START: {str(e)}"
            )
            sys.exit(1)

    async def start(self):
        """Start semua client userbot"""
        tasks = [
            self._start(client, i) for i, client in enumerate(self.clients, start=1)
        ]
        await asyncio.gather(*tasks)

    async def stop(self):
        """Stop semua client"""
        tasks = [client.stop() for client in self.clients]
        await asyncio.gather(*tasks)

    def on_message(self, filters=None, group=0):
        """Decorator handler pesan dengan error handling"""
        def decorator(func):
            @wraps(func)
            async def wrapper(client, message):
                try:
                    await func(client, message)
                except FloodWait as e:
                    LOGGER(__name__).warning(f"FLOOD WAIT {e.value}S")
                    await asyncio.sleep(e.value)
                except (ChatWriteForbidden, MessageNotModified, MessageIdInvalid):
                    pass
                except StopPropagation:
                    raise
                except Exception:
                    # Log error detail
                    err = traceback.format_exc()
                    log = (
                        f"ERROR USERBOT\n"
                        f"TIME: {datetime.now()}\n"
                        f"CHAT: {message.chat.id}\n"
                        f"USER: {message.from_user.id if message.from_user else 'UNKNOWN'}\n"
                        f"CMD/TEXT: {message.text}\n"
                        f"TRACE:\n{err}"
                    )
                    await client.send_message(config.LOG_GROUP_ID, log)
                    try:
                        await client.send_message(config.OWNER_ID[0], log)
                    except:
                        pass

            handler = MessageHandler(wrapper, filters)
            self.handlers.append((handler, group))
            return func
        return decorator

    async def idle(self):
        """Jaga userbot tetap running"""
        while True:
            await asyncio.sleep(5)

    def run(self):
        """Runner userbot"""
        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(self.start())
            loop.run_until_complete(self.idle())
        except KeyboardInterrupt:
            loop.run_until_complete(self.stop())
            LOGGER(__name__).info("USERBOT STOPPED")
            sys.exit(0)
        except Exception:
            LOGGER(__name__).error(traceback.format_exc())
            sys.exit(1)
