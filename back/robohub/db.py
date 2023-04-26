# aiohttpdemo_polls/db.py
from sqlalchemy import (
    MetaData, Table, Column, ForeignKey,
    Integer, String, Date
)
#import aiopg.sa
from sqlalchemy.ext.asyncio import create_async_engine


__all__ = ['roles', 'users']

meta = MetaData()

users = Table(
    'users', meta,

    Column('id', Integer, primary_key=True),
    Column('role_id',
           Integer,
           ForeignKey('roles.id', ondelete='CASCADE')),
    Column('email', String(200), nullable=False),
    Column('username', String(200), nullable=False),
    Column('hash', String(200), nullable=False),
)

jobs = Table(
    'jobs', meta,

    Column('id', Integer, primary_key=True),
    Column('user_id',
           Integer,
           ForeignKey('users.id', ondelete='CASCADE')),
    Column('name', String(200), nullable=False),
    Column('description', String(200), nullable=False),
    Column('job_status', Integer, nullable=False)

)

roles = Table(
    'roles', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(200), nullable=False),

)

robos = Table(
    'robos', meta,
    Column('id', Integer, primary_key=True),
    Column('titulo', String(200), nullable=False),
    Column('user_id',
               Integer,
               ForeignKey('users.id', ondelete='CASCADE')),
    Column('tipo', String(200), nullable=False),
    Column('ligado', Integer, nullable=False),
    Column('token', String(300), nullable=True),





)


async def get_user_by_name_sqlite(conn, username):
    result = await conn.execute(
        users
        .select()
        .where(users.c.username == username)
    )
    records =  result.fetchone() #delete AWAIT for sqlite
    return records

async def get_user_by_name(conn, username):
    result = await conn.execute(
        users
        .select()
        .where(users.c.username == username)
    )
    records =  await result.fetchone() #delete AWAIT for sqlite
    return records

        # minsize=conf['minsize'],
        # maxsize=conf['maxsize'],

def sqlite_context_engine(WORK_DIR):
    DB_DIR=WORK_DIR+'/robohub'
    print ('sqlite+aiosqlite:///{}/foo.db'.format(DB_DIR))
    engine =  create_async_engine('sqlite+aiosqlite:///{}/foo.db'.format(DB_DIR))
    return  engine

async def sqlite_context(app):
    WORK_DIR=app['config']['WORK_DIR']
    DB_DIR=WORK_DIR+'/robohub'
    engine = create_async_engine('sqlite+aiosqlite:///{}/foo.db'.format(DB_DIR))
    print ('sqlite+aiosqlite:///{}/foo.db'.format(DB_DIR))
    app['db'] = engine

    yield

    app['db'].close()
    await app['db'].wait_closed()

async def pg_context(app):
    conf = app['config']['postgres']
    engine = await aiopg.sa.create_engine(
        database=conf['DB_DATABASE'],
        user=conf['DB_USER'],
        password=conf['DB_PASSWD'],
        host=conf['DB_HOST'],
        port=conf['DB_PORT'],

    )
    app['db'] = engine

    yield

    app['db'].close()
    await app['db'].wait_closed()
