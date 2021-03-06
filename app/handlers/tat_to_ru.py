import logging 
import sqlite3 

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

import cmd
import keyboards


conn = sqlite3.connect("database/databasetg.db")
cursor = conn.cursor()
logger = logging.getLogger(__name__)

tat_alphabet=[]
a = ord('а')
for i in range(a,a+32):
    tat_alphabet.append(chr(i))
tat_alphabet.append(cmd.buttonO)
tat_alphabet.append(cmd.buttonE)
tat_alphabet.append(cmd.buttonZ)
tat_alphabet.append(cmd.buttonN)
tat_alphabet.append(cmd.buttonY)
tat_alphabet.append(cmd.buttonH)

ru_alphabet=[]
for i in range(a,a+32):
    ru_alphabet.append(chr(i))

def if_in_word(alphabet, word):
    word_array = []
    for i in word:
        word_array.append(i.lower())
    if list(filter(lambda i: i in word_array,alphabet)) != []:
        logger.info(f"COINCIDENCES: {list(filter(lambda i: i in word_array,alphabet))}")
        return 0


#<---Part with adding "add word" function--->
class TranslateWord(StatesGroup):
    waiting_for_tat_word = State()
    waiting_for_ru_word = State()

async def tat_word(message:types.Message):
    await message.answer("Слово на <b>татарском</b>:", reply_markup=keyboards.keyboard_tat_inline())
    await TranslateWord.waiting_for_tat_word.set()

async def tat_word_chosen(message:types.Message, state:FSMContext):
    global t_word
    if if_in_word(tat_alphabet,message.text.lower()) != 0:
        await message.answer("Пожалуйста, впишите слово на <b>татарском</b> языке")
        return
    t_word = message.text.lower()
    await state.update_data(chosen_tat_word=message.text.lower())
    await TranslateWord.waiting_for_ru_word.set()
    logger.info(f"TAT-WORD {message.text.upper()}")
    await message.answer("Отлично! Теперь впиши <b>русский</b> перевод:")

#ДОПИСАТЬ ОТПРАВКУ НУЖНЫХ БУКОВ
async def send_letter(call:types.CallbackQuery, state:FSMContext):
    await call.message.answer(cmd.buttonO)
    await call.message.answer(cmd.buttonE)
    await call.message.answer(cmd.buttonZ)
    await call.message.answer(cmd.buttonN)
    await call.message.answer(cmd.buttonY)
    await call.message.answer(cmd.buttonH)
    await call.answer()

async def ru_word_chosen(message:types.Message, state:FSMContext):
    if if_in_word(ru_alphabet,message.text.lower()) != 0:
        await message.answer("Пожалуйста, впишите слово на <b>русском</b> языке")
        return
    user_data = await state.get_data()
    para = [message.from_user.id, t_word, message.text.lower()]
    cursor.execute("select * from vocab")   
    if cursor.fetchall() == []:
        cursor.execute(f"INSERT INTO vocab VALUES (?,?,?)", para)
        logger.info(f"ADDED {para} TO DATABASE")
        conn.commit() 
        await message.answer(f"<i>Готово!</i>Вы добавили:\n<b>{user_data['chosen_tat_word']}</b> - {message.text.lower()}\n", reply_markup=keyboards.keyboard_main())
    else:
        cursor.execute("select * from vocab")      
        for i in cursor.fetchall():
            if i[1] == para[1]:
                await message.answer("Такое слово уже есть!", reply_markup=keyboards.keyboard_main())  
                logger.info(f"{para} ALREADY EXIST IN VOCAB")
                break 
            else:
                cursor.execute(f"INSERT INTO vocab VALUES (?,?,?)", para)
                logger.info(f"ADDED {para} TO DATABASE")  
                conn.commit() 
                await message.answer(f"<i>Готово!</i>Вы добавили:\n<b>{user_data['chosen_tat_word']}</b> - {message.text.lower()}\n", reply_markup=keyboards.keyboard_main())
                break
    conn.commit() 
    logger.info(f"RU-WORD {message.text.upper()}")
    await state.finish()

def register_handlers_tat_to_ru(dp: Dispatcher):
    dp.register_message_handler(tat_word, commands=["new", "neword", "newword", "add", "addword"], state="*")
    dp.register_message_handler(tat_word, Text(equals=cmd.buttonOne), state="*")
    dp.register_message_handler(tat_word_chosen, state=TranslateWord.waiting_for_tat_word)
    dp.register_message_handler(ru_word_chosen, state=TranslateWord.waiting_for_ru_word)
    dp.register_callback_query_handler(send_letter, Text(startswith="letter"), state="*")
