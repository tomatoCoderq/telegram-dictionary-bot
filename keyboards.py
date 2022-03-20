from aiogram import Bot, executor, types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import cmd 

def keyboard_main(keyboard):
    keyboard.add(types.KeyboardButton(text=cmd.buttonOne))
    keyboard.add(types.KeyboardButton(text=cmd.buttonTwo))