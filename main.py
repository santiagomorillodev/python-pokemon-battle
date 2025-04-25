from modules.get_pokemon_data import pokedex
from classes.pokemon_class import Character
from logic.battle_logic import battle

pokemon_1, data_1 =  pokedex()
pokemon_2, data_2 =  pokedex()
print(data_1)
character_1 = Character(pokemon_1, data_1['stats'][1]["attack"], data_1['stats'][0]["hp"], data_1['stats'][2]["defense"], data_1['attacks'], data_1['stats'][6]['type'])
character_2 = Character(pokemon_2, data_2['stats'][1]["attack"], data_2['stats'][0]["hp"], data_2['stats'][2]["defense"], data_2['attacks'], data_2['stats'][6]['type'])

battle(character_1, character_2)
