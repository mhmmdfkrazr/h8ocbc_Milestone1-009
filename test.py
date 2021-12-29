import json
import random
import config
from models import Directors, DirectorsSchema, Movies

connex_app = config.connex_app
connex_app.add_api('swagger.yml')
connex_app = connex_app.app

client = connex_app.test_client()

def test_director_read_all():
    url = '/api/director?limit=3'

    response = client.get(url)
    data = json.loads(response.get_data())
    assert isinstance(data, list) is True
    assert response.status_code == 200
    

def test_director_read_all_limit():
    limit = 253
    url = f'/api/director?limit={limit}'

    response = client.get(url)
    data = json.loads(response.get_data())

    assert response.status_code == 200
    assert len(data) == limit


def test_movie_read_all():
    url = '/api/movie?limit=3'

    response = client.get(url)
    data = json.loads(response.get_data())

    assert isinstance(data, list) is True
    assert response.status_code == 200


def test_movie_read_all_limit():
    limit = 322
    url = f'/api/movie?limit={322}'

    res = client.get(url)
    data = json.loads(res.get_data())

    assert res.status_code == 200
    assert len(data) == limit