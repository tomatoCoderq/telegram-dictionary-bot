from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

import cmd, logging, keyboards, sqlite3

conn = sqlite3.connect("database/databasetg.db")
cursor = conn.cursor()
logger = logging.getLogger(__name__)

async def list_of_words(message: types.Message):
    cursor.execute("select * from collections")
    await message.answer("Ваши подборки: ", reply_markup=keyboards.keyboard_create_inline())
    for i in cursor.fetchall():
        await message.answer("Ваши подборки:", reply_markup=keyboards.keyboard_generator(i[1]))


def register_handlers_my_words(dp: Dispatcher):
    dp.register_message_handler(list_of_words, Text(equals=cmd.buttonTwo))





    # cursor.execute("select * from vocab")
    # n = 0 
    # # print("AAAAJDAOKJDOAJDOIDJAOI")
    # # print(cursor.fetchall())
    # if len(cursor.fetchall()):
    #     cursor.execute("select * from vocab")
    #     for i in cursor.fetchall():
    #         await message.answer(f"{n}. {i[0]} - {i[1]}", reply_markup=keyboards.keyboard_main())
    #         logger.info(f"GOT FROM DATABASE: {n}. {i[0]} - {i[1]}")
    #         n+=1
    # else:
    #     await message.answer("Ваш словарик пустой!", reply_markup=keyboards.keyboard_main())
    #     logger.info("EMPTY")