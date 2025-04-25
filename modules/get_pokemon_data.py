from .get_attacks import get_pokemon_attacks
from .get_stats import get_pokemon_stats
from .style_name import style_name_attack
from os import system

def pokedex():
    while True:
        pokemon = input('Choose a pokemon: ')
        print(f'Buscando informacion de {pokemon}')
        attacks = get_pokemon_attacks(pokemon) # 👈🏼 extrayendo los nombres, poder y tipo de ataque
        stats = get_pokemon_stats(pokemon) # 👈🏼 extrayendo las estadisticas de los personaje como hp, attack, 
        if stats is None or attacks is None:
            print('No se encontraron datos')
        elif stats is False or attacks is False:
            print('Pokemon no encontrado')
        elif stats and attacks:
            system('cls')
            pokemon = style_name_attack(pokemon, stats[6]['type'])
            return [pokemon, {"attacks":attacks, "stats":stats}]
        