from cgitb import small
from aiogram import Bot, executor, types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import cmd

n = 0


def keyboard_main():
    buttons = [types.KeyboardButton(text=cmd.buttonOne),  
               types.KeyboardButton(text=cmd.buttonTwo)]
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    keyboard.add(*buttons)
    return keyboard


def keyboard_tat_inline():
    buttons_t = types.InlineKeyboardButton(text="Татарские буквы", callback_data="letter")
    keyboard_i = types.InlineKeyboardMarkup()
    keyboard_i.add(buttons_t)
    return keyboard_i

def keyboard_create_inline():
    button_c = types.InlineKeyboardButton(text="Создать подборку", callback_data="create_b")
    keyboard_c = types.InlineKeyboardMarkup()
    keyboard_c.add(button_c)
    return keyboard_c

def keyboard_generator(text_b=f"Подборка {n+1}"):
    global n
    button_g = [types.KeyboardButton(text=text_b, callback_data="create_1"),
    types.KeyboardButton(text=text_b, callback_data="create_2"),
    types.KeyboardButton(text=text_b, callback_data="create_3"),
    types.KeyboardButton(text=text_b, callback_data="create_4"),
    types.KeyboardButton(text=text_b, callback_data="create_5"),
    types.KeyboardButton(text=text_b, callback_data="create_6"),
    types.KeyboardButton(text=text_b, callback_data="create_7"),
    types.KeyboardButton(text=text_b, callback_data="create_8"),
    types.KeyboardButton(text=text_b, callback_data="create_9"),
    types.KeyboardButton(text=text_b, callback_data="create_10"),]
    keyboard_g = types.ReplyKeyboardMarkup(row_width=1)
    keyboard_g.add(*button_g)
    return keyboard_g  
    
