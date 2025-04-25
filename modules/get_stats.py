import requests

def fetch_stats_data(URL):
    response = requests.get(URL)
    response.raise_for_status()
    response = response.json()
    return response

def get_pokemon_stats(pokemon):
    try:
        stats = []
        URL = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
        response = fetch_stats_data(URL)
        
        for stat in response['stats']:
            name = stat['stat']['name']
            stats.append({name:stat['base_stat']})
        
        stats.append({'type': response['types'][0]['type']['name']})
        return stats
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return False
        else:
            print(f'HTTP Error: {e}')
    except TypeError as e:
        print('Type error')
    except requests.exceptions.RequestException as e:
        print(f'Error de conexion: {e}')
