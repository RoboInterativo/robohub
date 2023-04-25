from aiohttp import web
import aiohttp_jinja2
import jinja2
import logging
import yaml
import json
import jwt
import bcrypt
from robohub.auth import *
from robohub.db import pg_context,sqlite_context,sqlite_context_engine
from  robohub import db
from robohub.cloapi import *
from robohub.api import *
from os.path import exists
import asyncio
# from aiojobs.aiohttp import setup ,spawn

async def is_auth_handle(request):
    response=await validate(request)
    return  web.json_response(response)

async def logout_handle(request):
    exc = web.HTTPFound(location="/",body=json.dumps({'auth':False}) )
    exc.del_cookie("token")
    raise exc
async def git_login_handle (request):
    conf=request.app['config']

async def login_handle(request):
    conf=request.app['config']
    salt=conf['salt']
    salt=salt.decode('UTF8')
    post_data = await request.read()
    post_data=eval(post_data)
    #post_data_str=str(post_data_str,'UTF8')
    #post_data=json.loads(post_data_str)
    logging.info(post_data,str(type(post_data)))
    logging.info(post_data,str((post_data)))
    #1
    user=None
    # for item in conf['user_list']:
    #     if item['user']==post_data.get('username'):
    #         user=item
    username =post_data.get('username')
    if request.app['config']['mode']=='local':
        async with request.app['db'].begin() as conn:
            user = await db.get_user_by_name_sqlite(conn, username)
    else:
        async with request.app['db'].acquire() as conn:
            user = await db.get_user_by_name(conn, username)

        #stmt = select(user_table).where(user_table.c.name == 'spongebob')
        #records = await cursor.fetchall()
        #questions = [dict(q) for q in records]
    logging.info(f"config, {request.app['config']['mode']}")
    logging.info(f"user,{type(user)}")

    if user:
        password=bytes(post_data.get('password'),'UTF8')
        logging.info(f"hash,{user.hash}")

        if bcrypt.checkpw(password, bytes(user.hash,'UTF8') ):
            encoded_jwt = create_token ({"user": user.username,'id':user.id}, salt),
            logging.info("It Matches!")
            exc = web.HTTPFound(location="/",body=json.dumps ({'auth':True}))
            exc.set_cookie("token", encoded_jwt)
            raise exc
        else:
            logging.info("It Does not Match ")
            return web.json_response(json.dumps({'auth':False}))

            # exc = web.HTTPFound(location="/" )
            # #content_type='application/json',body=json.dumps({'auth':False})
            # exc=web.HTTPUnauthorized()
            # raise exc

    else:
        logging.info("user not found")
        return web.json_response(json.dumps({'auth':False}))

    # j=json.loads(jstr)
    #return web.json_response(json.dumps({'res':jstr}))



# async def get_files_handle(request):
#     files=get_files('/opt/app/')
#sdf


async def get_health_handle(request):
    conf=request.app['config']
    return web.json_response({'health':True})

async def get_robos_handle(request):

    conf=request.app['config']
    WORK_DIR= conf['WORK_DIR']


    response=await validate(request)
    if response.get('auth'):

        # cli_token=app['config']['token']
        # projects_id=get_project(cli_token)
        # if projects_id>0:
        #     images=get_images(cli_token,project_id)
        # else:
        #     images=[]

        logging.info('SEARCH in {}'.format(WORK_DIR))
        files=get_files(WORK_DIR+'/')
        # servers=get_servers(token)
        robos=[
        { "id": 1,
        "titulo":"my_first robo",
        "tipo":"telegram",
        "ligago":0        },
        {"id": 2,
        "titulo":"my_first robo 2",
        "tipo":"telegram",
        "ligago":0        },
        {"id": 3,
        "titulo":"my_first robo 3",
        "tipo":"telegram",
        "ligago":0       },
        {  "id": 4,
        "titulo":"my_first robo 4",
        "tipo":"telegram",
        "ligago":0        }
        ]
        # robos=[]
        return web.json_response({'auth':True,'robos':robos})
    else:
        return web.json_response({'auth':False,'error':response})








@aiohttp_jinja2.template('index.html')
async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name

    async def handler(request):
        return {}

def create_app(WORK_DIR):
    logging.info("Starting create APP.")
#    WORK_DIR=os.path.dirname(os.path.abspath(__file__))

    logging.info (f"Workdir{WORK_DIR}")

    CONF_DIR=WORK_DIR+'/robohub'

    #file_path = os.path.realpath(__file__)
    #os.path.dirname (file_path)
    conf_path= CONF_DIR+ '/conf.yml'
    logging.info(f"CONF PATH is {conf_path}")

    # if exists(conf_path):
    #     CONF_DIR=os.path.dirname (file_path)
    # elif exists('/opt/conf/conf.yml'):
    #     CONF_DIR='/opt/conf'
    # else:
    #     print (f'PATH {conf_path} not found')
    #     exit(-1)
    f=open(conf_path)
    STATIC_DIR=WORK_DIR+'/../front/build/'

    conf=yaml.safe_load(f)
    f.close()


    app = web.Application()



    logging.info('conf',conf)
    conf['WORK_DIR']=WORK_DIR
    conf['STATIC_DIR']=STATIC_DIR
    app['config']=conf

    if conf['mode']=='server':
        app.cleanup_ctx.append(pg_context)
    elif conf['mode']=='local':
        #logging.info("LINE 190 WORK_DIR", WORK_DIR )
        app['db']= sqlite_context_engine (WORK_DIR)
        # app.cleanup_ctx.append(sqlite_context)
        # sqlite_context_engine
# sqlite_context_engine
        # logging.info('STATIC',STATIC_DIR)
        # logging.info('PWD',WORK_DIR)
        # logging.info('CONF',WORK_DIR)
    aiohttp_jinja2.setup(app,
        loader=jinja2.FileSystemLoader(STATIC_DIR))



    app.add_routes([web.get('/', handle),
                    web.get('/api/health', get_health_handle),
                    web.post('/api/is_auth',is_auth_handle),
                    # web.post('/api/scheduler',scheduler_add ),
                    web.post('/api/robos',get_robos_handle),
                    web.post('/api/login',login_handle),
                    web.post('/api/github',git_login_handle),
                    web.post('/api/logout',logout_handle),
                    web.get('/{name}', handle),
                    web.static('/static', STATIC_DIR+'/static/')])
    #setup(app)
    return app

async def make_prediction():
    logging.info("START job")
    async with request.app['db'].begin() as conn:
        user = await db.get_user_by_name_sqlite(conn, username)
    # conn.execute(users.insert(), [
    #     {'username': 'admin', 'hash': hash_admin  ,
    #     'email': 'test1@robointerativo.ru','role_id':1},
    #     {'username': 'user', 'hash': hash_user ,
    #     'email': 'test2@robointerativo.ru','role_id':2},
    #     ])
    await asyncio.sleep(5.0)
    logging.info("DONE job")
    return 1

# async def scheduler_add(request):
#     await spawn(request, make_prediction())
#
#     return web.Response()


if __name__ == '__main__':

    # loop = asyncio.get_event_loop()
    try:
        logging.basicConfig(level=logging.DEBUG)
        WORK_DIR=os.path.dirname(os.path.abspath(__file__))+'/..'
        app =  create_app(WORK_DIR)
        web.run_app(app, host='0.0.0.0', port=5000)


        # logging.info(f"LOAD CONFIG ,DEPLOY MODE = {app['config']['mode']} " )
        # logging.info(f"STATIC_DIR= {app['config']['STATIC_DIR']} " )
        # logging.info(f"WORK_DIR= {app['config']['WORK_DIR']}  ")
    except Exception as e:
        logging.error("ERROR MAIN",str(e))
        # loop.stop()
