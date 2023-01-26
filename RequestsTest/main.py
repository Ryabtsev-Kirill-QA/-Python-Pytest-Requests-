import requests
import json

token = '1f623c0822adb5caeb52e674f568be6a'

response = requests.post('https://pokemonbattle.me:5000/pokemons', headers = {'Content-Type' : 'application/json', 'trainer_token' : token},
json = {
    "name": "Бульбаш",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"}
)

pokemon_id = response.json()['id']

print(response.text)

response_change = requests.put('https://pokemonbattle.me:5000/pokemons', headers = {'Content-Type' : 'application/json', 'trainer_token' : token},
json = {

    "pokemon_id": pokemon_id,
    "name": "Бараш",
    "photo": ""
}
)

print(response_change.text)

response_pokeball = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball', headers = {'Content-Type' : 'application/json', 'trainer_token' : token},
json = {
"pokemon_id": pokemon_id
}
)

print(response_pokeball.text)




