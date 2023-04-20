import pytest
import json
import asyncio
import aiohttp
#import requests
from robohub.main import *
from aiohttp import web, CookieJar



@pytest.fixture
def cli(loop, aiohttp_client):
    app=create_app()
    jar= CookieJar(unsafe=True,loop=loop)
    return loop.run_until_complete(aiohttp_client(app,cookie_jar=jar))


async def test_hello(cli):
    resp = await cli.post('/api/login',json={'username':'user','password':'user'
})
    assert resp.status == 200

async def test_validate(cli):
    resp = await cli.post('/api/login', json={'username':'user','password':'user'})
    assert resp.status == 200

    resp = await cli.post("/api/is_auth")
    assert resp.status == 200
    answ= await resp.json()
    assert answ['auth'] == True
    assert answ['data']['username'] == 'user'
    #text = await resp.text()
    #assert 'Hello, world' in text
async def test_health(cli):
    resp = await cli.get('/api/health', )
    assert resp.status == 200

    # resp = await cli.post("/api/profile")
    # assert resp.status == 200
    answ= await resp.json()
    assert answ['health'] == True

    #assert answ['data']['username'] == 'user'
async def test_profile(cli):
    resp = await cli.post('/api/login', json={'username':'user','password':'user'})
    assert resp.status == 200

    resp = await cli.post("/api/profile")
    assert resp.status == 200
    answ= await resp.json()
    assert answ['auth'] == True
    #assert answ['data']['username'] == 'user'
