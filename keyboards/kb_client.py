from aiogram.types import ReplyKeyboardMarkup, KeyboardButton #, ReplyKeyboardRemove
from database import sqlitedb



b1 = KeyboardButton('Суббота 10.00')
b2 = KeyboardButton('Суббота 12.00')
b3 = KeyboardButton('Суббота 14.00')
b4 = KeyboardButton('О нас')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).row(b2, b3).add(b4)

b1 = KeyboardButton('Расположение')
b2 = KeyboardButton('Время работы')
b3 = KeyboardButton('Цены')
b4 = KeyboardButton('Номер телефона')
b5 = KeyboardButton('Бесплатная индивидуальная тренировка')

kb_about = ReplyKeyboardMarkup(resize_keyboard=True)

kb_about.row(b1, b2).row(b3, b4).add(b5)