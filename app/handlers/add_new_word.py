import logging 
import sqlite3

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

import cmd
import keyboards

class Translation():
    def __init__(self, language_orig, language_translation, alphabet, cut):
        self.language_orig = language_orig
        self.language_translation = language_translation
        self.alphabet = alphabet
        self.cut = cut
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
        await state.update_data(chosen_word=message.text.lower())
        await TranslateWord.waiting_for_translation.set()
        self.logger.info(f"{self.cut}-WORD {message.text.upper()}")
        await message.answer(f"Отлично! Теперь впишите перевод на <b>{self.language_translation}</b>:")

    async def send_letters(self):
        None

    async def translation_chosen(self, message: types.Message, state: FSMContext):
        None

    def register_handlers_add_new_word(self, dp: Dispatcher):
        dp.register_message_handler(self.word_in_orig_language, commands=["new", "neword", "newword", "add", "addword"], state="*")
        dp.register_message_handler(self.word_in_orig_language, Text(equals=cmd.buttonOne), state="*")
        dp.register_message_handler(self.word_in_orig_language_chosen, state=TranslateWord.waiting_for_orig_word)
        dp.register_message_handler(self.translation_chosen, state=TranslateWord.waiting_for_translation)
        dp.register_callback_query_handler(self.send_letters, Text(startswith="letter"), state="*")

class TranslateWord(StatesGroup):
    waiting_for_orig_word = State()
    waiting_for_translation = State()
