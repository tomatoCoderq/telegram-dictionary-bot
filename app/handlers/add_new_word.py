import logging 
import sqlite3

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

import cmd
import keyboards

class Translation():
    def __init__(self, language_orig, language_translation, alphabet, cut_orig, cut_translation, db):
        self.language_orig = language_orig
        self.language_translation = language_translation
        self.alphabet = alphabet
        self.cut_orig = cut_orig
        self.cut_translation = cut_translation
        self.db = db
        self.on_start()
        
    def on_start(self):
        self.logger = logging.getLogger(__name__)
        self.conn = sqlite3.connect("database/databasetg.db")
        self.cursor = self.conn.cursor()
    
    def if_in_word(self, word):
        word_array = []
        for i in word:
            word_array.append(i.lower())
        if list(filter(lambda i: i in word_array,self.alphabet)) != []:
            self.logger.info(f"COINCIDENCES: {list(filter(lambda i: i in word_array,self.alphabet))}")
            return 0


    async def word_in_orig_language(self, message: types.Message):
        await message.answer(f"Введите слово на <b>{self.language_orig}</b> языке:", reply_markup=keyboards.keyboard_tat_inline())
        await TranslateWord.waiting_for_orig_word.set()

    async def word_in_orig_language_chosen(self, message: types.Message, state: FSMContext):
        if self.if_in_word(message.text.lower()) != 0:
            await message.answer(f"Пожалуйста, впишите слово на <b>{self.language_orig}</b> языке")
            return
        await state.update_data(chosen_orig=message.text.lower())
        await TranslateWord.waiting_for_translation.set()
        self.logger.info(f"{self.cut_orig}-WORD {message.text.upper()}")
        await message.answer(f"Отлично! Теперь впишите перевод на <b>{self.language_translation}</b>:")

    async def send_letters(self):
        None

    async def translation_chosen(self, message: types.Message, state: FSMContext):
        if self.if_in_word(message.text.lower()) != 0:
            await message.answer(f"Пожалуйста, впишите слово на <b>{self.language_translation}</b> языке")
            return
        user_data = await state.get_data()
        add_to_database = [message.from_user.id, user_data['chosen_orig'], message.text.lower()]
        self.cursor.execute(f"select * from {self.db}")   
        if self.cursor.fetchall() == []:
            self.cursor.execute(f"INSERT INTO {self.db} VALUES (?,?,?)", add_to_database)
            self.logger.info(f"ADDED {add_to_database} TO DATABASE {self.db}")
            self.conn.commit() 
            await message.answer(f"<i>Готово!</i>Вы добавили:\n<b>{user_data['chosen_orig']}</b> - {message.text.lower()}\n", reply_markup=keyboards.keyboard_main())
        else:
            self.cursor.execute(f"select * from {self.db}")    
            for i in self.cursor.fetchall():
                if i[1] == add_to_database[1]:
                    await message.answer("Такое слово уже есть!", reply_markup=keyboards.keyboard_main())  
                    self.logger.info(f"{add_to_database} ALREADY EXIST IN {self.db}")
                else:
                    print(i[1])
                    print(user_data['chosen_orig'])
                    self.cursor.execute(f"INSERT INTO {self.db} VALUES (?,?,?)", add_to_database)
                    self.logger.info(f"ADDED {add_to_database} TO DATABASE {self.db}")  
                    self.conn.commit() 
                    await message.answer(f"<i>Готово!</i>Вы добавили:\n<b>{user_data['chosen_orig']}</b> - {message.text.lower()}\n", reply_markup=keyboards.keyboard_main())
                    print("2")
                    break
        self.conn.commit() 
        self.logger.info(f"{self.cut_translation}-WORD {message.text.upper()}")
        await state.finish()

    def register_handlers_add_new_word(self, dp: Dispatcher):
        dp.register_message_handler(self.word_in_orig_language, commands=["new", "neword", "newword", "add", "addword"], state="*")
        dp.register_message_handler(self.word_in_orig_language, Text(equals=cmd.buttonOne), state="*")
        dp.register_message_handler(self.word_in_orig_language_chosen, state=TranslateWord.waiting_for_orig_word)
        dp.register_message_handler(self.translation_chosen, state=TranslateWord.waiting_for_translation)
        dp.register_callback_query_handler(self.send_letters, Text(startswith="letter"), state="*")

class TranslateWord(StatesGroup):
    waiting_for_orig_word = State()
    waiting_for_translation = State()
