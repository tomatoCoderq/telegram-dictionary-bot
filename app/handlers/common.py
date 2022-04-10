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


async def start(message:types.Message):
    await message.answer(f"""Привет, <b>{message.from_user.full_name}!</b>
Тебя приветствует <b>YourDictionaryBot</b>. YourDictionaryBot - это твой личный словарик, 
с помощью которого ты можешь заниматься изучением иностранных языков""", reply_markup=keyboards.keyboard_main())
    #await message.answer(f"Выбери язык, пожалуйста, для словарика\nP.S. Язык можно будет поменять командой \change", reply_markup=keyboards.inlineKeyboard_languages())
    logger.info(f"STARTED BY USER: {message.from_user.id}")

def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start", "hello", "welcome", "about"])


# dp.register_message_handler(cancel, commands="cancel", state="*")
# async def cancel(message: types.Message, state: FSMContext):
#     await state.finish()
#     await message.answer("Действие отменено", reply_markup=types.ReplyKeyboardRemove())
