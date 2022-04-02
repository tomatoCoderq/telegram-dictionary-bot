import sqlite3
import logging

from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.utils.exceptions import MessageTextIsEmpty

import cmd
import keyboards


class MyWords():
    def __init__(self, db):
        self.on_start()
        self.db = db

    def on_start(self):
        self.conn = sqlite3.connect("database/databasetg.db")
        self.cursor = self.conn.cursor()
        self.logger = logging.getLogger(__name__)


    async def words_list(self, message: types.Message):
        message_send = ''
        n = 1
        self.cursor.execute(f"select * from {self.db}")
        try:
            if len(self.cursor.fetchall()):
                self.cursor.execute(f"select * from {self.db}")
                for i in self.cursor.fetchall():
                    if i[0]==message.from_user.id:
                        message_send += f"{n}. <b>{i[1]}</b>-{i[2]}\n\n"
                        self.logger.info(f"GOT FROM DATABASE: {n}. {i[1]} - {i[2]}")
                        n+=1
                await message.answer(f"Ваши слова:\n\n{message_send}", reply_markup=keyboards.keyboard_main())
            else:
                await message.answer("Ваш словарик пустой!", reply_markup=keyboards.keyboard_main())
                self.logger.info("EMPTY")
        except MessageTextIsEmpty:
            await message.answer("Ваш словарик пустой! Добавьте слово", reply_markup=keyboards.keyboard_main())
    
    def register_handlers_my_words(self, dp:Dispatcher):
        dp.register_message_handler(self.words_list, Text(equals=cmd.buttonTwo))
