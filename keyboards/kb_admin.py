from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_message = KeyboardButton('Отправить всем напоминание')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_message)