from ast import Del
import sqlite3
import logging
import asyncio

from aiogram import Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from loguru import logger

from app.config_reader import load_config
from app.handlers.delete_words import register_handlers_delete
from app.handlers.my_words_old import register_handlers_my_words1
from app.handlers.common import register_handlers_common
from app.handlers.tat_to_ru import register_handlers_tat_to_ru
from app.handlers.add_new_word import Translation
from app.handlers.my_words import MyWords
from app.handlers.words_delete import DeleteWords
from app.handlers.change_language import LanguageMain
import cmd


def func(dp):
    langmain = LanguageMain()
    if langmain.man == cmd.tat:
        langmain.make(cmd.tat_lang_v2, cmd.ru_lang_v2, cmd.tat_alphabet(), cmd.ru_alphabet(), cmd.tat, cmd.ru, cmd.vocab_tat, dp)
        logger.info("Язык был изменён на татарский(tat)")
    if langmain.man == cmd.ger:
        langmain.make(cmd.ger_lang_v2, cmd.ru_lang_v2, cmd.ger_alphabet(), cmd.ru_alphabet(), cmd.ger, cmd.ru, cmd.vocab_ger, dp)
        logger.info("Язык был изменён на немецкий(ger)")
    if langmain.chosen_lang == cmd.eng:
        langmain.make(cmd.eng_lang_v2, cmd.ru_lang_v2, cmd.eng_alphabet(), cmd.ru_alphabet(), cmd.eng, cmd.ru, cmd.vocab_eng, dp)
    if langmain.chosen_lang == cmd.fr:
        langmain.make(cmd.fr_lang_v2, cmd.ru_lang_v2, cmd.fr_alphabet(), cmd.ru_alphabet(), cmd.fr, cmd.ru, cmd.vocab_fr, dp)
    if langmain.chosen_lang == cmd.sp:
        langmain.make(cmd.sp_lang_v2, cmd.ru_lang_v2, cmd.sp_alphabet(), cmd.ru_alphabet(), cmd.sp, cmd.ru, cmd.vocab_sp, dp)