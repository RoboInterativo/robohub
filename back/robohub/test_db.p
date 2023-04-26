# polls/init_db.py
from sqlalchemy import create_engine, MetaData

# from aiohttpdemo_polls.settings import config
from db import *

import bcrypt
import yaml
import os

# f=open('./conf.yml','w')
# f.write(yaml.dump(db ))




DSN = "postgresql://{DB_USER}:{DB_PASSWD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
def hashp (passwd,salt):
    return bcrypt.hashpw( passwd.encode('UTF8'),salt)


def delete_tables(engine):
    meta = MetaData()
    meta.drop_all(engine, [roles, users], checkfirst=True)

def create_tables(engine):
    meta = MetaData()
    meta.create_all(bind=engine, tables=[roles, users])


def sample_data(engine,config):
    conn = engine.connect()

    conn.execute(roles.insert(), [
        {'name': 'admin'},
        {'name': 'user'}

    ])

    salt=config['salt']
    print(salt, hashp('admin',salt))
    hash_user=hashp(u'user',salt).decode('UTF8')
    hash_admin=hashp(u'admin',salt).decode('UTF8')
    conn.execute(users.insert(), [
        {'username': 'admin', 'hash': hash_admin  ,
        'email': 'test1@robointerativo.ru','role_id':1},
        {'username': 'user', 'hash': hash_user ,
        'email': 'test2@robointerativo.ru','role_id':2},
        ])

    conn.close()


if __name__ == '__main__':
    config_postgres={}
    for item in ['DB_USER','DB_PASSWD','DB_HOST','DB_PORT','DB_DATABASE']:
        config_postgres[item] = os.environ[item]
    config={'postgres':config_postgres}
    config['salt']=bcrypt.gensalt(10)
    f=open('/opt/conf.yml','w')
    f.write(yaml.dump(config ))
    f.close()

    db_url = DSN.format(**config['postgres'])
    engine = create_engine(db_url)

    delete_tables(engine)
    create_tables(engine)
    sample_data(engine,config)
