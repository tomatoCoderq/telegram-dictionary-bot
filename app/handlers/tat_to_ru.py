from cgitb import text
from email import message
from itertools import chain
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

import cmd, logging, keyboards



logger = logging.getLogger(__name__)

ru_alphabet=[]
a = ord('а')
for i in range(a,a+32):
    ru_alphabet.append(chr(i))
print(ru_alphabet)

tat_alphabet=[]
for i in range(a,a+32):
    tat_alphabet.append(chr(i))
tat_alphabet.append(chr(1257))
tat_alphabet.append(chr(1241))
tat_alphabet.append(chr(1175))
tat_alphabet.append(chr(1187))
tat_alphabet.append(chr(1199))
tat_alphabet.append(chr(1211))
print(tat_alphabet)


class TranslateWord(StatesGroup):
    waiting_for_ru_word = State()
    waiting_for_tat_word = State()

async def ru_word(message:types.Message):
    await message.answer("Слово на <b>русском</b>:")
    await TranslateWord.waiting_for_ru_word.set()

async def ru_word_chosen(message:types.Message, state:FSMContext):
    await state.update_data(chosen_ru_word=message.text.lower())
    await TranslateWord.waiting_for_tat_word.set()
    messageR = message.text.lower()
    logger.info(f"RU-WORD {message.text.upper()}")
    await message.answer("Отлично! Теперь впиши <b>татарский</b> перевод:", reply_markup=keyboards.keyboard_tat_inline())

async def send_letter(call:types.CallbackQuery):
    await call.message.answer("OK")
    print("OK")
    await call.answer()

async def tat_word_chosen(message:types.Message, state:FSMContext):
    messageT = message.text.lower()
    user_data = await state.get_data()
    await message.answer(f"{user_data['chosen_ru_word']} - {message.text.lower()}\n")
    await message.answer("Добавлено! Можешь добавить больше слов.", )
    logger.info(f"TAT-WORD {message.text.upper()}")
    await state.finish()

def register_handlers_tat_to_ru(dp: Dispatcher):
    dp.register_message_handler(ru_word, Text(equals=cmd.buttonOne), state="*")
    dp.register_message_handler(ru_word_chosen, state=TranslateWord.waiting_for_ru_word)
    dp.register_message_handler(tat_word_chosen, state=TranslateWord.waiting_for_tat_word)
    dp.register_callback_query_handler(send_letter, Text(endswith="o"))
    dp.register_callback_query_handler(send_letter, Text(endswith="e"))