import asyncio
from distutils.command.config import config
from json import load
from aiogram import Bot, executor, types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import sqlite3
import logging

from app.config_reader import load_config
from app.handlers.my_words import register_handlers_my_words
logger = logging.getLogger(__name__)

import cmd
from app.handlers.common import register_handlers_common
from app.handlers.tat_to_ru import register_handlers_tat_to_ru

#ПРОПИСАТЬ ЛОГГИНГ

async def main():
    logging.basicConfig(
        level = logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.error("Starting bot")

    config = load_config('config/main.ini')

    bot = Bot(token = config.tg_bot.token, parse_mode=types.ParseMode.HTML)
    dp = Dispatcher(bot, storage=MemoryStorage())

    conn = sqlite3.connect("databasetg.db")
    cursor = conn.cursor()

    # cursor.execute("CREATE TABLE IF NOT EXISTS vocab(word, translation)")
    # conn.commit()

    register_handlers_tat_to_ru(dp)
    register_handlers_common(dp)
    register_handlers_my_words(dp)

    # await set_commands(bot)

    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())