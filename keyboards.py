from aiogram import types

import cmd 


def keyboard_main():
    buttons = [types.KeyboardButton(text=cmd.buttonOne),  
               types.KeyboardButton(text=cmd.buttonTwo),
               types.KeyboardButton(text=cmd.buttonThree)
    ]
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    keyboard.add(*buttons)
    return keyboard

def keyboard_tat_inline():
    buttons_t = [types.InlineKeyboardButton(text="✍️Татарские буквы✍️", callback_data="letter")]
    keyboard_i = types.InlineKeyboardMarkup()
    keyboard_i.add(*buttons_t)
    return keyboard_i
