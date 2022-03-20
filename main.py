from aiogram import Bot, executor, types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

import sqlite3
import cmd

#ПРОПИСАТЬ ЛОГГИНГ

bot = Bot(token="5287896214:AAE6tyQqjUrggIoRAPGWMuFgYdQwmyu5m2M", parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

conn = sqlite3.connect("databasetg.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS vocab(word, translation)")
conn.commit()

def keyboard_main(keyboard):
    keyboard.add(types.KeyboardButton(text=cmd.buttonOne))
    keyboard.add(types.KeyboardButton(text=cmd.buttonTwo))
   

@dp.message_handler(commands=['start', 'welcome', 'about'])
async def start(message:types.Message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    keyboard_main(keyboard)
    await message.answer("НАПИСАТЬ ПРИВЕТСТВЕННОЕ СООБЩЕНИЕ. О ЧЁМ, ЗАЧЕМ. ДОБАВИТЬ ИНЛАЙН КНОПКИ", reply_markup=keyboard)
    

@dp.message_handler(Text(equals=cmd.buttonOne))
async def new_word(message:types.Message):
    print(message.text)
    await message.answer("Напиши слово на русском языке и перевод на английском")

@dp.message_handler(Text)
async def get_word(message:types.Message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    keyboard_main(keyboard)
    msg = message.text
    list = msg.split()
    ru = list[0]
    eng = list[1]
    cursor.execute("""INSERT INTO vocab 
                  VALUES("{ru}", "{eng}")
                  """)
    conn.commit()
    await message.answer("Найс", reply_markup=keyboard)  


@dp.message_handler(Text(equals=cmd.buttonTwo))
async def words_list(message:types.Message):
    cursor.execute("SELECT * FROM vocab;")
    print(cursor.fetchone())



if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)