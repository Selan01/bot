from aiogram.utils import executor

from create_bot import dp

from handlers import client, admin, other
from database import sqlitedb

async def on_startup(_):
    print('Бот вышел в online')
    sqlitedb.sql_user()

client.register_handlers_client(dp)
admin.register_handler_admin(dp)
other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
