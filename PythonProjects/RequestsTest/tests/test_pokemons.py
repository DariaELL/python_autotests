import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
Token = '5503f10416a0497cb2d982322ed573b6'
Header = {'content_type':'application_json','trainer_token': Token}
TRAINER_ID = '36115'

def test_status_code():
    response_trainers = requests.get(url = f'{URL}/trainers', headers = Header)
    assert response_trainers.status_code == 200

def test_trainer():
    response_trainers_spisok = requests.get(url = f'{URL}/trainers', headers = Header, params = {'trainer_id' : TRAINER_ID})
    assert response_trainers_spisok.json()['data'][0]['id'] == '36115'
    