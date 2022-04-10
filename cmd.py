#Common words and commands
buttonOne = "✏️Добавить слово✏️"
buttonTwo = "📔Мои слова📔"
buttonThree = "🗑Удалить слово🗑"


#Tatar language
buttonO = chr(1257)
buttonE = chr(1241)
buttonZ = chr(1175)
buttonN = chr(1187)
buttonY = chr(1199)
buttonH = chr(1211)
tat_lang_v1 = "татарский"
tat_lang_v2 = "татарском"
tat = "TAT"
vocab_tat = "vocab_tat"

def tat_alphabet():
    tat_alphabet=[]
    a = ord('а')
    for i in range(a,a+32):
        tat_alphabet.append(chr(i))
    tat_alphabet.append(buttonO)
    tat_alphabet.append(buttonE)
    tat_alphabet.append(buttonZ)
    tat_alphabet.append(buttonN)
    tat_alphabet.append(buttonY)
    tat_alphabet.append(buttonH)
    return tat_alphabet


#German language
ger_lang_v1 = "немецкий"
ger_lang_v2 = "немецком"
ger = "GER"
vocab_ger = "vocab_ger"

def ger_alphabet():
    ger_alphabet = []
    a = ord('a')
    for i in range(a, a+26):
        ger_alphabet.append(chr(i))
    ger_alphabet.append(chr(228))
    ger_alphabet.append(chr(246))
    ger_alphabet.append(chr(252))
    ger_alphabet.append(chr(223))
    return ger_alphabet
print(ger_alphabet())


#English language
eng_lang_v1 = "английский"
eng_lang_v2 = "английском"
eng = "ENG"
vocab_eng = "vocab_eng"

def eng_alphabet():
    eng_alphabet = []
    a = ord('a')
    for i in range(a, a+26):
        eng_alphabet.append(chr(i))
    return eng_alphabet


#French language 
fr_lang_v1 = "французский"
fr_lang_v2 = "французском"
fr = "FR"
vocab_fr = "vocab_fr"

def french_alphabet():
    french_alphabet = []
    a = ord('a')
    for i in range(a, a+26):
        french_alphabet.append(chr(i))
    return french_alphabet


#Spanish language 
sp_lang_v1 = "испанский"
sp_lang_v2 = "испанском"
sp = "SP"
vocab_sp = "vocab_sp"

def spanish_alphabet():
    spanish_alphabet = []
    a = ord('a')
    for i in range(a, a+26):
        spanish_alphabet.append(chr(i))
    spanish_alphabet.append(chr(241))
    return spanish_alphabet


#Russian language
ru_lang_v1 = "русский"
ru_lang_v2 = "русском"
ru = "RU"

def ru_alphabet():
    ru_alphabet=[]
    a = ord('а')
    for i in range(a,a+32):
        ru_alphabet.append(chr(i))
    return ru_alphabet
