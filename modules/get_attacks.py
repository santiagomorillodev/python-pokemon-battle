import requests, random
from modules.style_name import style_name_attack
def fetch_attack_data(URL):
    try:
        response = requests.get(URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        if e.response.status_code == 404:
            print('Recurso no encontrado (404).')
            return False
        print(f'HTTP Error: {e}')
    except requests.exceptions.RequestException as e:
        print(f'Error de conexion: {e}')
        
def process_move(move):
    name = move['move']['name']
    URL_ATTACK = move["move"]["url"]
    response_attack = fetch_attack_data(URL_ATTACK)
    type_attack = response_attack['type']['name'] # 👈🏼 Puede ser usado para la infromacion del ataqu
    power = response_attack.get("power")
    if not response_attack:
        return None, None, None
    return name, power, type_attack



def get_pokemon_attacks(pokemon):
    count = 0
    try:
        attacks = []
        URL = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
        response = fetch_attack_data(URL)
        moves = response['moves']
        random.shuffle(moves)
        
        for move in moves:
            if len(attacks) == 6:
                break
            
            name, power, type_attack = process_move(move)
            if power is None:
                continue
            if name not in attacks:
                name = style_name_attack(name, type_attack)
                attacks.append({"name": name, "power": power,"type": type_attack})
            
            count += 1
        return attacks
    except TypeError as e:
        print('Type error')
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print('Recurso no encontrado (404).')
            return False
        print(f'HTTP Error: {e}')
    except requests.exceptions.RequestException as e:
        print(f'Error de conexión: {e}')