import sqlite3
import logging
import asyncio

from aiogram import Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from app.config_reader import load_config
from app.handlers.delete_words import register_handlers_delete
from app.handlers.my_words import register_handlers_my_words
from app.handlers.common import register_handlers_common
from app.handlers.tat_to_ru import register_handlers_tat_to_ru
from app.handlers.add_new_word import Translation
import cmd


logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level = logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.error("Starting bot")

    config = load_config('config/main.ini')

    bot = Bot(token = config.tg_bot.token, parse_mode=types.ParseMode.HTML)
    dp = Dispatcher(bot, storage=MemoryStorage())

    conn = sqlite3.connect("database/databasetg.db")
    cursor = conn.cursor()

    tr = Translation(cmd.tat_lang_v2, cmd.ru_lang_v2, cmd.tat_alphabet_1, cmd.tat)

    cursor.execute("CREATE TABLE IF NOT EXISTS vocab_tat(id, word, translation)")
    cursor.execute("CREATE TABLE IF NOT EXISTS vocab_german(id, word, translation)")
    cursor.execute("CREATE TABLE IF NOT EXISTS vocab_eng(id, word, translation)")
    cursor.execute("CREATE TABLE IF NOT EXISTS vocab_spanish(id, word, translation)")
    cursor.execute("CREATE TABLE IF NOT EXISTS vocab_french(id, word, translation)")


    # register_handlers_tat_to_ru(dp)
    register_handlers_common(dp)
    register_handlers_my_words(dp)
    register_handlers_delete(dp)
    register_handlers_tat_to_ru(dp)
    # tr.register_handlers_add_new_word(dp)
    

    # await set_commands(bot)

    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())