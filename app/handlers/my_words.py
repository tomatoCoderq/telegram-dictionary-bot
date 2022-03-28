from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

import cmd, logging, keyboards, sqlite3

conn = sqlite3.connect("database/databasetg.db")
cursor = conn.cursor()
logger = logging.getLogger(__name__)

async def list_of_words(message: types.Message):
    message_send = ''
    n = 0 
    cursor.execute("select * from vocab")
    if len(cursor.fetchall()):
        cursor.execute("select * from vocab")
        for i in cursor.fetchall():
            message_send += f"{n}. <b>{i[0]}</b>-{i[1]}\n\n"
            logger.info(f"GOT FROM DATABASE: {n}. {i[0]} - {i[1]}")
            n+=1
        await message.answer(message_send, reply_markup=keyboards.keyboard_main())

    else:
        await message.answer("Ваш словарик пустой!", reply_markup=keyboards.keyboard_main())
        logger.info("EMPTY")

def register_handlers_my_words(dp: Dispatcher):
    dp.register_message_handler(list_of_words, Text(equals=cmd.buttonTwo))

