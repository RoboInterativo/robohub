# import pytest
#
# import json
import asyncio
import logging
# # from pytes-sanic import sanic
# import aiohttp
# #import requests
from robohub.main import *
from aiohttp import web, CookieJar
from aiohttp.test_utils import TestClient, TestServer, loop_context
#
#
# from aiohttp.test_utils import TestClient, TestServer
import uvloop
#
# import pytest
# from aiohttp import web

from aiohttp import web
logging.basicConfig(level=logging.DEBUG)
with loop_context() as loop:
    WORK_DIR=os.path.dirname(os.path.abspath(__file__))+'/..'
    print (WORK_DIR)
    logging.info('WORK_DIR',WORK_DIR)
    app = create_app(WORK_DIR)
    jar= CookieJar(unsafe=True,loop=loop)
    port=5000
    client = TestClient(TestServer(app), loop=loop,cookie_jar=jar)
    loop.run_until_complete(client.start_server())
    root = "http://127.0.0.1:{}".format(port)

    # async def test_get_route():
    #     resp = await client.get("/")
    #
    #     assert resp.status == 200
    async def test_hello(client):
        resp = await cli.post('/api/login',json={'username':'user','password':'user'
    })
        assert resp.status == 200
    # text = await resp.text()
    # assert "Hello, world" in text

#
# async def hello(request):
#     return web.Response(body=b"Hello, world")

# @pytest.yield_fixture()
# def event_loop():
#     uvloop.install()
#     loop = asyncio.new_event_loop()
#     assert isinstance(loop, uvloop.Loop)
#     yield loop
#     loop.close()

# def create_app():
#     app = web.Application()
#     app.router.add_route("GET", "/", hello)
#     return app
#
#
# async def test_hello(aiohttp_client):
#     client = await aiohttp_client(await create_app())
#     resp = await client.get("/")
#     assert resp.status == 200
#     text = await resp.text()
#     assert "Hello, world" in text

#
# @pytest.fixture
# def test_cli(loop, app, sanic_client):
#     return loop.run_until_complete(sanic_client(app))
# with loop_context() as loop:
#     app = create_app()
#     async def test_index(test_cli):
#         resp = await test_cli.get('/')
#         assert resp.status_code == 200

# async def previous(request):
#     if request.method == 'POST':
#         request.app['value'] = (await request.post())['value']
#         return web.Response(body=b'thanks for the data')
#     return web.Response(
#         body='value: {}'.format(request.app['value']).encode('utf-8'))
#
# @pytest.fixture
# def cli(loop, aiohttp_client):
#     app = web.Application()
#     app.router.add_get('/', previous)
#     app.router.add_post('/', previous)
#     return loop.run_until_complete(aiohttp_client(app))
#
# async def test_set_value(cli):
#     resp = await cli.post('/', data={'value': 'foo'})
#     assert resp.status == 200
#     assert await resp.text() == 'thanks for the data'
#     assert cli.server.app['value'] == 'foo'
#
# async def test_get_value(cli):
#     cli.server.app['value'] = 'bar'
#     resp = await cli.get('/')
#     assert resp.status == 200
#     assert await resp.text() == 'value: bar'


#
# # asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
# # with loop_context() as loop:
# #     app = create_app()
# #     jar= CookieJar(unsafe=True,loop=loop)
# #     client = TestClient(TestServer(app), loop=loop,cookie_jar=jar)
# #     loop.run_until_complete(client.start_server())
# #     root = "http://127.0.0.1:{}".format(port)
# #
# #     async def test_get_route():
# #         resp = await client.get("/")
# #         assert resp.status == 200
# #         # text = await resp.text()
# #         # assert "Hello, world" in text
# #
# #     loop.run_until_complete(test_get_route())
# #     loop.run_until_complete(client.close())
#
#
# # asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
#
#
# @pytest.fixture
# def cli(loop, aiohttp_client):
#     app=create_app()
#     jar= CookieJar(unsafe=True,loop=loop)
#     return loop.run_until_complete(aiohttp_client(app,cookie_jar=jar))
#
# #
# #
# async def test_hello(cli):
#     resp = await cli.post('/api/login',json={'username':'user','password':'user'
# })
#     assert resp.status == 200
# #
# # async def test_validate(cli):
# #     resp = await cli.post('/api/login', json={'username':'user','password':'user'})
# #     assert resp.status == 200
# #
# #     resp = await cli.post("/api/is_auth")
# #     assert resp.status == 200
# #     answ= await resp.json()
# #     assert answ['auth'] == True
# #     assert answ['data']['username'] == 'user'
# #     #text = await resp.text()
# #     #assert 'Hello, world' in text
# # async def test_health(cli):
# #     resp = await cli.get('/api/health', )
# #     assert resp.status == 200
# #
# #     # resp = await cli.post("/api/profile")
# #     # assert resp.status == 200
# #     answ= await resp.json()
# #     assert answ['health'] == True
# #
# #     #assert answ['data']['username'] == 'user'
# # async def test_profile(cli):
# #     resp = await cli.post('/api/login', json={'username':'user','password':'user'})
# #     assert resp.status == 200
# #
# #     resp = await cli.post("/api/profile")
# #     assert resp.status == 200
# #     answ= await resp.json()
# #     assert answ['auth'] == True
#     #assert answ['data']['username'] == 'user'
