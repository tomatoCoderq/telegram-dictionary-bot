from cgitb import text
from distutils.util import execute
from email import message
from glob import glob
from itertools import chain
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

import cmd, logging, keyboards, sqlite3

conn = sqlite3.connect("database/databasetg.db")
cursor = conn.cursor()
logger = logging.getLogger(__name__)

async def list_of_words(message: types.Message):
    cursor.execute("select * from vocab")
    n=0
    for i in cursor.fetchmany():
        await message.answer(f"{n}. {i[n]} - {i[n+1]}", reply_markup=keyboards.keyboard_main())
        print(f"{n}. {i[n]} - {i[n+1]}")
        n+=1
    # conn.commit()

def register_handlers_my_words(dp: Dispatcher):
    dp.register_message_handler(list_of_words, Text(equals=cmd.buttonTwo))

