from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from cv2 import add
from loguru import logger

from app.handlers.add_new_word import Translation
from app.handlers.my_words import MyWords
from app.handlers.words_delete import DeleteWords
import keyboards
import cmd 


# def tat_language():
#     add_new = Translation(cmd.tat_lang_v2, cmd.ru_lang_v2, cmd.tat_alphabet(), cmd.tat, cmd.ru, cmd.vocab_tat)
#     my_words = MyWords(cmd.vocab_tat)
#     delete = DeleteWords(cmd.vocab_tat)
#     return add_new, my_words, delete
    
# def german_language():
#     add_new = Translation(cmd.ger_lang_v2, cmd.ru_lang_v2, cmd.german_alphabet(), cmd.ger, cmd.ru, cmd.vocab_ger)
#     my_words = MyWords(cmd.vocab_ger)
#     delete = DeleteWords(cmd.vocab_ger)

# def eng_language():
#     add_new = Translation(cmd.eng_lang_v2, cmd.ru_lang_v2, cmd.eng_alphabet(), cmd.eng, cmd.ru, cmd.vocab_eng)
#     my_words = MyWords(cmd.vocab_eng)
#     delete = DeleteWords(cmd.vocab_eng)

# def french_language():
#     add_new = Translation(cmd.fr_lang_v2, cmd.ru_lang_v2, cmd.french_alphabet(), cmd.fr, cmd.ru, cmd.vocab_fr)
#     my_words = MyWords(cmd.vocab_fr)
#     delete = DeleteWords(cmd.vocab_fr)



class LanguageMain():
    man = cmd.ger
    def __init__(self):
        self.chosen_lang = "1"

    def make(self, language_orig, language_translation, alphabet, alphabet_orig, cut_orig, cut_translation, db, dp):
        logger.debug("make_start")
        add_new =  Translation(language_orig, language_translation, alphabet, alphabet_orig,cut_orig, cut_translation, db)
        my_words = MyWords(db)
        delete = DeleteWords(db)
        add_new.register_handlers_add_new_word(dp) 
        my_words.register_handlers_my_words(dp) 
        delete.register_handlers_delete(dp)
        logger.debug("make_end")


    async def change_language(self, message:types.Message):
        await message.answer(f"Выбери язык, пожалуйста, для словарика", reply_markup=keyboards.inlineKeyboard_languages())
        await Choice.waiting_for_language.set()

    async def choosen_language(self, call: types.CallbackQuery, state: FSMContext):
        usinglanguage = ""
        if call.data == "l1":
            man = cmd.tat
            usinglanguage = "1"
            await call.answer()
        elif call.data == "l2":
            self.chosen_lang = cmd.ger
            usinglanguage = "2"
            await call.answer()
        elif call.data == "l3":
            self.chosen_lang = cmd.eng
            usinglanguage = "3"
            await call.answer()
        elif call.data == "l4":
            self.chosen_lang = cmd.fr
            usinglanguage = "4"
            await call.answer()
        elif call.data == "l5":
            self.chosen_lang = cmd.sp
            usinglanguage = "5"
            await call.answer()
        await call.message.answer(f"Отлично! Вы выбрали ТАКОЙ_ТО ЯЗЫК. Если хотите его поменять, то снова пропишите /change. ")
        await state.finish()

    def register_handlers_change(self, dp: Dispatcher):
        logger.debug(self.chosen_lang)
        dp.register_message_handler(self.change_language, commands="change")
        dp.register_callback_query_handler(self.choosen_language, state=Choice.waiting_for_language)


class Choice(StatesGroup):
    waiting_for_language = State()




