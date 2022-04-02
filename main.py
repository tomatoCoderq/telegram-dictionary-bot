from ast import Del
import sqlite3
import logging
import asyncio

from aiogram import Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from app.config_reader import load_config
from app.handlers.delete_words import register_handlers_delete
from app.handlers.my_words_old import register_handlers_my_words1
from app.handlers.common import register_handlers_common
from app.handlers.tat_to_ru import register_handlers_tat_to_ru
from app.handlers.add_new_word import Translation
from app.handlers.my_words import MyWords
from app.handlers.words_delete import DeleteWords
from app.handlers.change_language import register_handlers_change
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

    tr = Translation(cmd.tat_lang_v2, cmd.ru_lang_v2, cmd.tat_alphabet(), cmd.tat, cmd.ru, cmd.vocab_tat)
    my = MyWords(cmd.vocab_tat)
    dlt = DeleteWords(cmd.vocab_tat)

    cursor.execute("CREATE TABLE IF NOT EXISTS vocab_tat(id, word, translation)")
    cursor.execute("CREATE TABLE IF NOT EXISTS vocab_ger(id, word, translation)")
    cursor.execute("CREATE TABLE IF NOT EXISTS vocab_eng(id, word, translation)")
    cursor.execute("CREATE TABLE IF NOT EXISTS vocab_sp(id, word, translation)")
    cursor.execute("CREATE TABLE IF NOT EXISTS vocab_fr(id, word, translation)")


    # register_handlers_tat_to_ru(dp)
    register_handlers_common(dp)
    my.register_handlers_my_words(dp)
    # register_handlers_delete(dp)
    tr.register_handlers_add_new_word(dp)
    dlt.register_handlers_delete(dp)
    register_handlers_change(dp)
    

    # await set_commands(bot)

    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())