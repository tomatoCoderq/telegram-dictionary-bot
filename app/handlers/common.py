from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from cv2 import add


from app.handlers.add_new_word import Translation
from app.handlers.my_words import MyWords
from app.handlers.words_delete import DeleteWords
import keyboards
import cmd


def tat_language():
    add_new = Translation(cmd.tat_lang_v2, cmd.ru_lang_v2, cmd.tat_alphabet(), cmd.tat, cmd.ru, cmd.vocab_tat)
    my_words = MyWords(cmd.vocab_tat)
    delete = DeleteWords(cmd.vocab_tat)
    return add_new, my_words, delete
    
def german_language():
    add_new = Translation(cmd.ger_lang_v2, cmd.ru_lang_v2, cmd.german_alphabet(), cmd.ger, cmd.ru, cmd.vocab_ger)
    my_words = MyWords(cmd.vocab_ger)
    delete = DeleteWords(cmd.vocab_ger)

def eng_language():
    add_new = Translation(cmd.eng_lang_v2, cmd.ru_lang_v2, cmd.eng_alphabet(), cmd.eng, cmd.ru, cmd.vocab_eng)
    my_words = MyWords(cmd.vocab_eng)
    delete = DeleteWords(cmd.vocab_eng)

def french_language():
    add_new = Translation(cmd.fr_lang_v2, cmd.ru_lang_v2, cmd.french_alphabet(), cmd.fr, cmd.ru, cmd.vocab_fr)
    my_words = MyWords(cmd.vocab_fr)
    delete = DeleteWords(cmd.vocab_fr)

def spanish_language():
    add_new = Translation(cmd.sp_lang_v2, cmd.ru_lang_v2, cmd.spanish_alphabet(), cmd.sp, cmd.ru, cmd.vocab_sp)
    my_words = MyWords(cmd.vocab_sp)
    delete = DeleteWords(cmd.vocab_sp)

class Choice(StatesGroup):
    waiting_for_language = State()

async def start(message:types.Message):
    await message.answer(f"""Привет, <b>{message.from_user.full_name}!</b>
Тебя приветствует <b>YourDictionaryBot</b>. YourDictionaryBot - это твой личный словарик, 
с помощью которого ты можешь заниматься изучением иностранных языков""")
    await message.answer(f"Выбери язык, пожалуйста, для словарика\nP.S. Язык можно будет поменять командой \change", reply_markup=keyboards.inlineKeyboard_languages())
    await Choice.waiting_for_language.set()

async def choosen_language(call: types.CallbackQuery, state: FSMContext):
    if call.data== "l1":
        tat_language
    elif call.data == "l2":
        german_language()
    elif call.data == "l3":
        eng_language()
    elif call.data == "l4":
        french_language()
    elif call.data == "l5":
        spanish_language()
        
    await call.answer()
    await state.finish()
# async def cancel(message: types.Message, state: FSMContext):
#     await state.finish()
#     await message.answer("Действие отменено", reply_markup=types.ReplyKeyboardRemove())

def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start", "hello", "welcome", "about"])
    dp.register_callback_query_handler(choosen_language, state=Choice.waiting_for_language)
    # dp.register_message_handler(cancel, commands="cancel", state="*")

