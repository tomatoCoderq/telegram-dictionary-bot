from aiogram import Bot, executor, types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import cmd, keyboards


async def start(message:types.Message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    keyboards.keyboard_main(keyboard)
    await message.answer(f"""Привет, <b>{message.from_user.full_name}!</b>
Тебя приветствует <b>YourDictionaryBot</b>. YourDictionaryBot - это твой личный словарик, 
с помощью которого ты можешь заниматься изучением иностранных языков""", reply_markup=keyboard)

async def cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Действие отменено", reply_markup=types.ReplyKeyboardRemove())

def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start", "hello", "welcome", "about"])
    dp.register_message_handler(cancel, commands="cancel", state="*")

