from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text


import cmd, logging, keyboards, sqlite3

conn = sqlite3.connect("database/databasetg.db")
cursor = conn.cursor()
logger = logging.getLogger(__name__)

class DeleteWord(StatesGroup):
    waiting_for_number = State()


async def get_number(message: types.Message):
    message_send = ''
    n = 1
    cursor.execute("select * from vocab")
    if len(cursor.fetchall()):
        await message.answer("Какое слово вы хотите <b>удалить</b>?Напишите, пожалуйста, <i>это слово на русском или татарском</i>")
        cursor.execute("select * from vocab")
        for i in cursor.fetchall():
            if i[0]==message.from_user.id:
                message_send += f"{n}. <b>{i[1]}</b>-{i[2]}\n\n"
                logger.info(f"GOT FROM DATABASE: {n}. {i[1]} - {i[2]}")
                n+=1
        await message.answer(message_send, reply_markup=keyboards.keyboard_main())
        await DeleteWord.waiting_for_number.set()

    else:
        await message.answer("Ваш словарик пустой!", reply_markup=keyboards.keyboard_main())
        logger.info("EMPTY")
    
async def delete_word(message:types.Message, state:FSMContext):
    delete_s = ''
    cursor.execute("select * from vocab")
    for i in cursor.fetchall():
        if i[0]==message.from_user.id:
            if message.text.lower() == i[1]:
                delete = message.text.lower()
                delete_s += delete
                cursor.execute("DELETE FROM vocab WHERE word=?", (delete,))
                await message.answer(f"<i>Готов!</i>\n<b>{delete}</b> было удалено", reply_markup=keyboards.keyboard_main())
            elif message.text.lower() == i[2]:
                delete = message.text.lower()
                cursor.execute("DELETE FROM vocab WHERE translation=?", (delete,))
                await message.answer(f"<i>Готов!</i>\n<b>{delete}</b> было удалено", reply_markup=keyboards.keyboard_main())
    conn.commit()
    await state.finish()


def register_handlers_delete(dp: Dispatcher):
    dp.register_message_handler(get_number, Text(equals=cmd.buttonThree), state="*")
    dp.register_message_handler(delete_word, state=DeleteWord.waiting_for_number)

