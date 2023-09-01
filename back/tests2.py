from sqlalchemy import create_engine, MetaData, Integer, String, Column, Table, select
from sqlalchemy.orm import Session
import os
import bcrypt

def hash_pass(password):
    ''' Хеширует пароль и возвращает хэш '''
    hashAndSalt = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashAndSalt

def isValidatePass(password, hashedPassword):
    ''' Сверяет хэш и правильный пароль, возвращает True или False '''
    valid = bcrypt.checkpw(password.encode(), hashedPassword)
    return valid

# Создаем два хэша из паролей пользователей
u1_pass = str(hash_pass('1234'))
u2_pass = str(hash_pass('4321'))

# Переменные которые содержат пути
WORK_DIR = os.getcwd()
DIR_DB = os.path.join(WORK_DIR, 'test.db')

# Инициализируем движок, указываем где будет находиться БД
engine = create_engine(f'sqlite:///{DIR_DB}')
session = Session(bind=engine)

# Подключение к БД
conn = engine.connect()

# Метаданные
metadata = MetaData()

# Создаем Таблицу users
users = Table('users', metadata,
    Column('user_id', Integer, primary_key=True),
    Column('username', String(200)),
    Column('hash', String(200))
)

metadata.create_all(engine)

insert_query = users.insert().values([
    {'username': 'Weagook', 'hash': u1_pass},
    {'username': 'MetaWeag', 'hash': u2_pass}
])

conn.execute(insert_query)

select_all_query = select(users)
select_all_result = conn.execute(select_all_query)

print(select_all_result.fetchall())
