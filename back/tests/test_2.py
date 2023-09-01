<<<<<<< HEAD
import pytest
import json
import asyncio
import aiohttp
#import requests
from robohub import *
from aiohttp import web, CookieJar

import logging
logging.basicConfig(level=logging.DEBUG)



# WORK_DIR=os.path.dirname(os.path.abspath(__file__))+'/..'
# app=create_app(WORK_DIR)
# jar=  CookieJar(unsafe=True,loop=loop)


from aiohttp.test_utils import TestClient, TestServer, loop_context
from aiohttp import request
from robohub.main import *


# loop_context is provided as a utility. You can use any
# asyncio.BaseEventLoop class in its place.
# with loop_context() as loop:
#     WORK_DIR=os.path.dirname(os.path.abspath(__file__))+'/..'

#     app=create_app(WORK_DIR)
#     jar=  CookieJar(unsafe=True,loop=loop)

#     print (WORK_DIR)
#     logging.info('WORK_DIR',WORK_DIR)

#
#     with TestClient(TestServer(app), loop=loop) as client:
#
#         async def test_get_route():
#             #nonlocal client

#             resp = await client.get("/api/login")

#             resp = await client.get("/")

#             assert resp.status == 200
#             # text = await resp.text()
#             # assert "Hello, world" in text
#
#         loop.run_until_complete(test_get_route())

#============


from aiohttp.test_utils import TestClient, TestServer, loop_context

with loop_context() as loop:
    WORK_DIR=os.path.dirname(os.path.abspath(__file__))+'/..'
    app = create_app(WORK_DIR)

    client = TestClient(TestServer(app), loop=loop)
    loop.run_until_complete(client.start_server())
    port =5000



from aiohttp.test_utils import TestClient, TestServer

with loop_context() as loop:
    WORK_DIR=os.path.dirname(os.path.abspath(__file__))+'/..'
    print (WORK_DIR)
    logging.info('WORK_DIR',WORK_DIR)
    app = create_app(WORK_DIR)
    port=5000

    client = TestClient(TestServer(app), loop=loop)
    loop.run_until_complete(client.start_server())

    root = "http://127.0.0.1:{}".format(port)

    async def test_get_route():
        resp = await client.get("/")
        assert resp.status == 200
        # text = await resp.text()
        # assert "Hello, world" in text

    loop.run_until_complete(test_get_route())
    loop.run_until_complete(client.close())
