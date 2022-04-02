from ast import Del
from app.handlers.add_new_word import Translation
from app.handlers.my_words import MyWords
from app.handlers.words_delete import DeleteWords
import cmd

def tat_language():
    add_new = Translation(cmd.tat_lang_v2, cmd.ru_lang_v2, cmd.tat_alphabet(), cmd.tat, cmd.ru, cmd.vocab_tat)
    my_words = MyWords(cmd.vocab_tat)
    delete = DeleteWords(cmd.vocab_tat)
    
def german_language():
    add_new = Translation(cmd.ger_lang_v2, cmd.ru_lang_v2, cmd.alphabet, cmd.ger, cmd.ru, cmd.vocab_ger)
    my_words = MyWords(cmd.vocab_ger)
    delete = DeleteWords(cmd.vocab_ger)

def eng_language():
    add_new = Translation(cmd.eng_lang_v2, cmd.ru_lang_v2, cmd.alphabet, cmd.eng, cmd.ru, cmd.vocab_eng)
    my_words = MyWords(cmd.vocab_eng)
    delete = DeleteWords(cmd.vocab_eng)

def french_language():
    add_new = Translation(cmd.fr_lang_v2, cmd.ru_lang_v2, cmd.alphabet, cmd.fr, cmd.ru, cmd.vocab_fr)
    my_words = MyWords(cmd.vocab_fr)
    delete = DeleteWords(cmd.vocab_fr)

def spanish_language():
    add_new = Translation(cmd.sp_lang_v2, cmd.ru_lang_v2, cmd.alphabet, cmd.sp, cmd.ru, cmd.vocab_sp)
    my_words = MyWords(cmd.vocab_sp)
    delete = DeleteWords(cmd.vocab_sp)

#АЛФАВИИИИИТ