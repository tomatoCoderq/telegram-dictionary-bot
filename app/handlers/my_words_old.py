import sqlite3
import logging

from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.utils.exceptions import MessageTextIsEmpty

import cmd
import keyboards


conn = sqlite3.connect("database/databasetg.db")
cursor = conn.cursor()
logger = logging.getLogger(__name__)

async def list_of_words(message: types.Message, db):
        message_send = ''
        n = 1
        cursor.execute(f"select * from {cmd.db}")
        try:
            if len(cursor.fetchall()):
                cursor.execute("select * from vocab")
                for i in cursor.fetchall():
                    if i[0]==message.from_user.id:
                        message_send += f"{n}. <b>{i[1]}</b>-{i[2]}\n\n"
                        logger.info(f"GOT FROM DATABASE: {n}. {i[1]} - {i[2]}")
                        n+=1
                await message.answer(message_send, reply_markup=keyboards.keyboard_main())
            else:
                await message.answer("Ваш словарик пустой!", reply_markup=keyboards.keyboard_main())
                logger.info("EMPTY")
        except MessageTextIsEmpty:
            await message.answer("Ваш словарик пустой! Добавьте слово", reply_markup=keyboards.keyboard_main())

def register_handlers_my_words1(dp: Dispatcher):
    dp.register_message_handler(list_of_words, Text(equals=cmd.buttonTwo))

