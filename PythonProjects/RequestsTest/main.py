import requests

URL = 'https://api.pokemonbattle.ru/v2'
Token = '5503f10416a0497cb2d982322ed573b6'
Header = {'content_type':'application_json','trainer_token': Token}
Body_create = {
    "name": "generate",
    "photo_id": -1
}


response_create = requests.post(url = f'{URL}/pokemons',headers = Header, json = Body_create)
print(response_create.text)
pokemon = response_create.json()['id']
print(pokemon)


Body_change = {
    "pokemon_id": pokemon,
    "name": "generate",
    "photo_id": -1
}

response_change = requests.put(url = f'{URL}/pokemons', headers = Header, json = Body_change)
print(response_change.text)
print(response_change.status_code)

Body_catch = {
    "pokemon_id": pokemon
}


response_change = requests.post(url = f'{URL}/trainers/add_pokeball', headers = Header, json = Body_change)
print(response_change.text)

response_trainers = requests.get(url = f'{URL}/trainers', headers = Header)
print(response_trainers.text)

TRAINER_ID = '36115'

response_trainers_spisok = requests.get(url = f'{URL}/trainers', headers = Header, params = {'trainer_id' : TRAINER_ID})
print(response_trainers_spisok.text)

