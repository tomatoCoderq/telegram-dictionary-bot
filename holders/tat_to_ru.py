from itertools import chain
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

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
    await message.answer("Введите слово на русском")
    await TranslateWord.waiting_for_russian_word.set()

async def ru_word_chosen(message:types.Message, state:FSMContext):
    await state.update_data(chosen_ru_word=message.text.lower())
    await TranslateWord.next()
    await message.answer("Теперь выберите татарское слово")

async def tat_word_chosen(message:types.Message, state:FSMContext):
    user_data = await state.get_data()
    await message.answer(f"Вы вписали слово {message.text.lower()} {user_data['chosen_ru_word']}.\n")
    await state.finish()

def register_handlers_food(dp: Dispatcher):
    dp.register_message_handler(ru_word, commands="food", state="*")
    dp.register_message_handler(ru_word_chosen, state=TranslateWord.waiting_for_ru_word)
    dp.register_message_handler(tat_word_chosen, state=TranslateWord.waiting_for_tat_word)