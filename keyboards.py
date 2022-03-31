from cgitb import small
from aiogram import Bot, executor, types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import cmd

n = 0
buttons_g = []


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
    global buttons_g
    buttons_g = []
    keyboard_g = types.ReplyKeyboardMarkup(row_width=1)
    # keyboard_g.add(*buttons_g)
    return keyboard_g

def add_in_array(message):
    global buttons_g
    buttons_g += message
    print(buttons_g)
    keyboard_main().add(*buttons_g)
    return keyboard_main()
    
