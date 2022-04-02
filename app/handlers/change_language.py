from aiogram import types, Dispatcher
import keyboards


async def change_language(message:types.Message):
    await message.answer(f"Выбери язык, пожалуйста, для словарика", reply_markup=keyboards.keyboard_languages())

def register_handlers_change(dp: Dispatcher):
    dp.register_message_handler(change_language, commands="change")
