from aiogram import types, Dispatcher
from datetime import datetime

from create_bot import bot
from keyboards.kb_client import kb_client, kb_about
from database import sqlitedb


#@dp.message_handler(commands=['регистрация'])
async def command_register(message: types.Message):
    try:
        id = await sqlitedb.sql_examination(message.from_user.id)
        if(id):
            await bot.send_message(message.from_user.id, 'Вы уже зарегистрированы', reply_markup=kb_about)
        else:
            first_name = message.from_user.first_name
            last_name = message.from_user.last_name
            user_id = message.from_user.id
            joining_date = datetime.now()
            joining_date = '%s/%s/%s' % (joining_date.month, joining_date.day, joining_date.year)
            sign_up = 'NO'
            sing_up_data = 0
            day_time = 0
            data = (first_name, last_name, user_id, joining_date, sign_up, sing_up_data, day_time)
            await sqlitedb.sql_add_person(data)
            await bot.send_message(message.from_user.id, 'Здравствуйте', reply_markup=kb_client)
    except Exception as e:
        await message.reply(e)

#@dp.message_handler(commands='Записаться')
async def sign_up_person(message: types.Message):
    ex = await sqlitedb.sql_examination(message.from_user.id)
    if(ex[1] == 'YES'):
        await bot.send_message(message.from_user.id, 'Вы уже записаны', reply_markup=kb_about)
    else:
        day_time = message.text
        print(message.text)
        user_id = message.from_user.id
        sign_up = 'YES'
        sign_up_date = datetime.now()
        sign_up_date = '%s/%s/%s' % (sign_up_date.month, sign_up_date.day, sign_up_date.year)
        print(sign_up_date)
        data1 = (sign_up, user_id)
        data2 = (sign_up_date, user_id)
        data3 = (day_time, user_id)
        print(data1[0],data1[1])
        await sqlitedb.sql_sign_up(data1, data2, data3)
        await bot.send_message(message.from_user.id, 'Вы записаны', reply_markup=kb_about)
        info = await sqlitedb.sql_info(message.from_user.id)
        info = ' '.join(info)
        await bot.send_message(message.from_user.id, info)


async def sparta_about(message: types.Message):
    await bot.send_message(message.from_user.id, 'Полезная информация', reply_markup=kb_about)
async def sparta_location(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул Победы д 1')

async def sparta_work_time(message: types.Message):
    await bot.send_message(message.from_user.id, 'Time')

async def sparta_price(message: types.Message):
    await bot.send_message(message.from_user.id, 'Цены')

async def sparta_support(message: types.Message):
    await bot.send_message(message.from_user.id, 'Номер телефона')

async def sparta_reserved(message: types.Message):
    await bot.send_message(message.from_user.id, 'Бесплатная тренировка', reply_markup=kb_client)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_register, lambda message: '/start' in message.text)
    dp.register_message_handler(sign_up_person, lambda message: 'Суббота' in message.text)
    dp.register_message_handler(sparta_location, lambda message: 'Расположение' in message.text)
    dp.register_message_handler(sparta_work_time, lambda message: 'Время работы' in message.text)
    dp.register_message_handler(sparta_price, lambda message: 'Цены' in message.text)
    dp.register_message_handler(sparta_support, lambda message: 'Номер телефона' in message.text)
    dp.register_message_handler(sparta_about, lambda message: 'О нас' in message.text)
    dp.register_message_handler(sparta_reserved, lambda message: 'Бесплатная индивидуальная тренировка' in message.text)