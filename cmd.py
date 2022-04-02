#Common words and commands
from re import T


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
tat_alphabet_1 = []
tat_alphabet_1 += tat_alphabet

#German language
ger_lang_v1 = "немецкий"
ger_lang_v2 = "немецком"
ger = "GER"

#English language
eng_lang_v1 = "английский"
eng_lang_v2 = "английском"
eng = "ENG"

#French language 
fr_lang_v1 = "французский"
fr_lang_v2 = "французском"
fr = "FR"

#Spanish language 
sp_lang_v1 = "испанский"
sp_lang_v2 = "испанском"
sp = "SP"

#Russian language
ru_lang_v1 = "русский"
ru_lang_v2 = "русском"