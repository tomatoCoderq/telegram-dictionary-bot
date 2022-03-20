import asyncio
from distutils.command.config import config
from aiogram import Bot, executor, types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import sqlite3

import cmd
from handlers.common import register_handlers_common
from handlers.tat_to_ru import register_handlers_tat_to_ru

#ПРОПИСАТЬ ЛОГГИНГ
async def main():
    bot = Bot(token = "5287896214:AAE6tyQqjUrggIoRAPGWMuFgYdQwmyu5m2M", parse_mode=types.ParseMode.HTML)
    dp = Dispatcher(bot, storage=MemoryStorage())

    conn = sqlite3.connect("databasetg.db")
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS vocab(word, translation)")
    conn.commit()

    register_handlers_tat_to_ru(dp)
    register_handlers_common(dp)
    # register_handlers_more(dp)

    # await set_commands(bot)

    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())