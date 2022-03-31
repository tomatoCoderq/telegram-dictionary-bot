from asyncio.log import logger
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

import cmd, logging, keyboards, sqlite3

logger = logging.getLogger(__name__)
conn = sqlite3.connect("database/databasetg.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS collections(user, collection)")

class NewCollections(StatesGroup):
    waiting_for_name = State()

async def new_collect(call:types.CallbackQuery):
    await call.message.answer(f"Введите, пожалуйста, название новой подборки.\nЛучше использовать короткии названия")
    await NewCollections.waiting_for_name.set()
    await call.answer()


async def collections_name(message:types.Message, state:FSMContext):
    para_1 = [message.from_user.id, message.text.lower()]
    ifok = cursor.execute(f"INSERT INTO collections VALUES (?,?)", para_1)
    conn.commit()
    if ifok:
        logger.info(f"ADDED TO DATABASE {para_1}")
        await message.answer(f"Отлично! Вы создали подборку под названием <b>{message.text.lower()}</b>", reply_markup=keyboards.keyboard_main())
        logger.info(f"MADE COLLECTION IS CALLED {message.text.upper()}")
    await state.finish()


def register_handlers_add_new_collect(dp:Dispatcher):
    dp.register_callback_query_handler(new_collect, Text(equals="create_b"), state="*")
    dp.register_message_handler(collections_name, state=NewCollections.waiting_for_name)
