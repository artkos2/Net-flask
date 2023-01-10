import requests
from tests.test_db import create_ad
from tests.url_config import URL


def test_root():
    resp = requests.get(URL)
    assert resp.status_code == 404


def test_get_ad_by_id(create_ad):
    new_ad = create_ad
    resp = requests.get(f'{URL}/ads/{new_ad["id"]}')
    assert resp.status_code == 200
    data = resp.json()
    assert data['title'] == new_ad['title']

def test_get_ad_not_ex(create_ad):
    resp = requests.get(f'{URL}/ads/774545')
    assert resp.status_code == 404

def test_create_ad():
    resp = requests.post(f'{URL}/ads/', json={"user_id": 10, "title": "Шкаф для десткой", "description": "Новый"})
    assert resp.status_code == 200
    json_data = resp.json()
    assert json_data['title'] == 'Шкаф для десткой'

def test_delete_ad():
    resp = requests.post(f'{URL}/ads/', json={"user_id": 10, "title": "Шкаф для десткой2"})
    assert resp.status_code == 200
    json_data = resp.json()
    resp = requests.delete(f'{URL}/ads/{json_data["id"]}')
    assert resp.status_code == 200
    resp = requests.get(f'{URL}/ads/{json_data["id"]}')
    assert resp.status_code == 404

def test_patch_ad():
    resp = requests.post(f'{URL}/ads/', json={"user_id": 10, "title": "Шкаф"})
    assert resp.status_code == 200
    json_data = resp.json()
    resp = requests.patch(f'{URL}/ads/{json_data["id"]}', json={"title": "Шкаф332"})
    assert resp.status_code == 200
    resp = requests.get(f'{URL}/ads/{json_data["id"]}')
    json_data = resp.json()
    assert resp.status_code == 200
    assert json_data['title'] == 'Шкаф332'
