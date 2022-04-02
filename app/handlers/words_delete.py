import logging
import sqlite3

from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

import cmd

from httpx import delete
import keyboards

class DeleteWords():
    def __init__(self, db):
        self.db = db
        self.on_start()


    def on_start(self):
        self.conn = sqlite3.connect("database/databasetg.db")
        self.cursor = self.conn.cursor()
        self.logger = logging.getLogger(__name__)

    async def get_word(self, message: types.Message):
        message_send = ''
        n = 1
        self.cursor.execute(f"select * from {self.db}")
        if len(self.cursor.fetchall()):
            await message.answer(f"Какое слово вы хотите <b>удалить</b>?Напишите, пожалуйста, <i>это слово на русском или {cmd.tat_lang_v2}</i>")
            self.cursor.execute(f"select * from {self.db}")
            for i in self.cursor.fetchall():
                if i[0]==message.from_user.id:
                    message_send += f"{n}. <b>{i[1]}</b>-{i[2]}\n\n"
                    self.logger.info(f"GOT FROM DATABASE: {n}. {i[1]} - {i[2]}")
                    n+=1
            await message.answer(message_send, reply_markup=keyboards.keyboard_main())
            await DeleteProcessing.waiting_for_word.set()

        else:
            await message.answer("Ваш словарик пустой!", reply_markup=keyboards.keyboard_main())
            self.logger.info("EMPTY")
    
    async def delete_word(self, message: types.Message, state: FSMContext):
        delete_s = ''
        self.cursor.execute(f"select * from {self.db}")
        for i in self.cursor.fetchall():
            if i[0]==message.from_user.id:
                if message.text.lower() == i[1]:
                    delete = message.text.lower()
                    delete_s += delete
                    self.cursor.execute(f"DELETE FROM {self.db} WHERE word=?", (delete,))
                    await message.answer(f"<i>Готово!</i>\n<b>{delete}</b> было удалено", reply_markup=keyboards.keyboard_main())
                elif message.text.lower() == i[2]:
                    delete = message.text.lower()
                    self.cursor.execute(f"DELETE FROM {self.db} WHERE translation=?", (delete,))
                    await message.answer(f"<i>Готово!</i>\n<b>{delete}</b> было удалено", reply_markup=keyboards.keyboard_main())
        self.conn.commit()
        await state.finish()
    
    def register_handlers_delete(self, dp: Dispatcher):
        dp.register_message_handler(self.get_word, Text(equals=cmd.buttonThree), state="*")
        dp.register_message_handler(self.delete_word, state=DeleteProcessing.waiting_for_word)

class DeleteProcessing(StatesGroup):
    waiting_for_word = State()