# polls/init_db.py
from sqlalchemy import create_engine, MetaData
import sys

# from aiohttpdemo_polls.settings import config
from robohub.db import *

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
<<<<<<< HEAD
    meta.drop_all(engine, [roles, users], checkfirst=True)

def create_tables(engine):
    meta = MetaData()
    meta.create_all(bind=engine, tables=[roles, users])
=======
    meta.drop_all(engine, [roles, users, platforms, bots], checkfirst=True)

def create_tables(engine):
    meta = MetaData()
    meta.create_all(bind=engine, tables=[roles, users, platforms, bots])
>>>>>>> 2156b49b18f9e7a7ab3fbbecf980d80df2b29451


def sample_data(engine,config):
    print ("CREATE DATA")
    conn = engine.connect()

    result=conn.execute(roles.insert(), [
        {'name': 'admin'},
        {'name': 'user'}

    ])
    print (result)

    salt=config['salt']
    print(salt, hashp('admin',salt))
    hash_user=hashp(u'user',salt).decode('UTF8')
    hash_admin=hashp(u'admin',salt).decode('UTF8')
    try:
        conn.execute(users.insert(), [
            {'username': 'admin', 'hash': hash_admin  ,
            'email': 'test1@robointerativo.ru','role_id':1},
            {'username': 'user', 'hash': hash_user ,
            'email': 'test2@robointerativo.ru','role_id':2},
            ])
        conn.commit()
        conn.close()
    except (e):
        print(e)

def main(argv):
    file_path = os.path.realpath(__file__)
    print (file_path )
    print (os.path.dirname (file_path))
    CONF_DIR=os.path.dirname (file_path)



    if argv[1] =='local':
        print ("CREATE LOCAL")
        config={}
        config['salt']=bcrypt.gensalt(10)

        #sqlite_context_engine(CONF_DIR)
        config['mode']='local'
        CONF_DIR=os.path.dirname (file_path)
        print (f'write {CONF_DIR}/conf.yml  ')
        f=open(CONF_DIR+'/conf.yml','w')
        f.write(yaml.dump(config ))
        f.close()
        print (f'sqlite:///{CONF_DIR}/foo.db')
        engine = create_engine(f'sqlite:///{CONF_DIR}/foo.db')
        delete_tables(engine)
        create_tables(engine)
        sample_data(engine,config)
    else:
        print ('DEPLOYMENT MODE')
        config={}
        config['salt']=bcrypt.gensalt(10)
        config['mode']='server'
        config_postgres={}
        for item in ['DB_USER','DB_PASSWD','DB_HOST','DB_PORT','DB_DATABASE']:
            config_postgres[item] = os.environ[item]
            config={'postgres':config_postgres}
            config['mode']='server'
            config['salt']=bcrypt.gensalt(10)

        db_url = DSN.format(**config['postgres'])
        #config['db_url']=db_url
        engine = create_engine(db_url)
    #config['token']=os.environ['VDS_TOKEN']






        f=open(CONF_DIR+'/conf.yml','w')
        f.write(yaml.dump(config ))
        f.close()
        delete_tables(engine)
        create_tables(engine)
        sample_data(engine,config)


if __name__ == '__main__':
    if len( sys.argv)>1:
        main(sys.argv)
