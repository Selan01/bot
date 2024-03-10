import sqlite3 as sq



# Вносим в базу пользователей
def sql_user():
    global base, cur
    base = sq.connect('sparta.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!!!!!!!!')
    base.execute('CREATE TABLE IF NOT EXISTS person(first_name TEXT, last_name TEXT ,user_id TEXT, joining_date TEXT, sign_up TEXT, sign_up_date TEXT, day_time TEXT)')


async def sql_add_person(data):
    cur.execute('INSERT INTO person VALUES(?,?,?,?,?,?, ?)', data)
    base.commit()


async def sql_sign_up(data1, data2, data3):
    cur.execute(f"UPDATE person SET sign_up = ? where user_id = ?", data1)
    cur.execute(f"UPDATE person SET sign_up_date = ? where user_id = ?", data2)
    cur.execute(f"UPDATE person SET sign_up_date = ? where user_id = ?", data3)
    base.commit()


async def sql_examination(user_id):
    return cur.execute('SELECT user_id, sign_up FROM person WHERE user_id == ?', (user_id,)).fetchone()

async def sql_message():
    try:
        return cur.execute("SELECT user_id FROM person WHERE sign_up LIKE 'NO'")
    except Exception:
        pass


async def sql_info(user_id):
    return cur.execute('SELECT first_name, last_name, sign_up_date, user_id  FROM person WHERE user_id == ?', (user_id,)).fetchone()


