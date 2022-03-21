from aiogram import Bot, executor, types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import cmd 

def keyboard_main():
    buttons = [types.KeyboardButton(text=cmd.buttonOne),  
               types.KeyboardButton(text=cmd.buttonTwo)]
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    keyboard.add(*buttons)
    return keyboard


def keyboard_tat_inline():
    buttons_t = [types.InlineKeyboardButton(text=cmd.buttonO, callback_data="letter_o"),
                types.InlineKeyboardButton(text=cmd.buttonE, callback_data="letter_e"),
                types.InlineKeyboardButton(text=cmd.buttonZ, callback_data="letter_z"),
                types.InlineKeyboardButton(text=cmd.buttonN, callback_data="letter_n"),
                types.InlineKeyboardButton(text=cmd.buttonY, callback_data="letter_y"),
                types.InlineKeyboardButton(text=cmd.buttonH, callback_data="letter_h")]
    keyboard_i = types.InlineKeyboardMarkup()
    keyboard_i.add(*buttons_t)
    return keyboard_i
