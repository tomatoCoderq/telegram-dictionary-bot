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

def inlineKeyboard_languages():
    buttons_l = [types.InlineKeyboardButton(text=cmd.tat_lang_v1, callback_data="l1"),
                 types.InlineKeyboardButton(text=cmd.ger_lang_v1, callback_data="l2"),
                 types.InlineKeyboardButton(text=cmd.eng_lang_v1, callback_data="l3"),
                 types.InlineKeyboardButton(text=cmd.fr_lang_v1, callback_data="l4"),
                 types.InlineKeyboardButton(text=cmd.sp_lang_v1, callback_data="l5")
                ]
    keyboard_l = types.InlineKeyboardMarkup(row_width=1)
    keyboard_l.add(*buttons_l)
    return keyboard_l
