from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from create_bot import bot
from database import sqlitedb
from keyboards import kb_admin

ID = None

class FSMAdmin(StatesGroup):
    date=State()


#Получаем ID текущего иодератора
async def make_change_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Готов исполнить любой приказ, Хозяйка', reply_markup=kb_admin.button_case_admin)
    await message.delete()


async def send_mess(message: types.Message):
    try:
        persons = await sqlitedb.sql_message()
        for item in persons:
            print(item)
            await bot.send_message(int(item[0]), 'Напоминание')
    except Exception:
        await bot.send_message(1091233895, 'Таких нет')

def register_handler_admin(dp: Dispatcher):
    dp.register_message_handler(make_change_command,Text(equals='Хозяйка',ignore_case=True),is_chat_admin=True)
    dp.register_message_handler(send_mess, lambda message: 'напоминание' in message.text)

