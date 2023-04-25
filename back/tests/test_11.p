from robohub.main import *
async def test_hello(aiohttp_client):
    WORK_DIR=os.path.dirname(os.path.abspath(__file__))+'/..'
    print (WORK_DIR)
    logging.info('WORK_DIR',WORK_DIR)
    app = create_app(WORK_DIR)
    client = await aiohttp_client(app)
    resp = await client.get("/")
    assert resp.status == 200
    # text = await resp.text()
    # assert "Hello, world" in text

# """Tests module."""
#
# from unittest import mock
# from robohub.main import *
#
# @pytest.fixture
# def app():
#     app = create_app()
#     yield app
#     app.container.unwire()
#
# @pytest.fixture
# def client(app, aiohttp_client, loop):
#     return loop.run_until_complete(aiohttp_client(app))
#
# async def test_index_no_data(client, app):
#     giphy_client_mock = mock.AsyncMock(spec=GiphyClient)
#     giphy_client_mock.search.return_value = {
#         "data": [],
#     }
#
#     with app.container.giphy_client.override(giphy_client_mock):
#         response = await client.get("/")
#
#     assert response.status == 200
#     data = await response.json()
#     assert data["gifs"] == []
