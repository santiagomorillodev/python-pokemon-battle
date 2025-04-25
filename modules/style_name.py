def style_name_attack(name, type_attack):
    type_to_emoji = {
        'normal': '🐾',
        'fire': '🔥',
        'water': '💧',
        'electric': '⚡',
        'grass': '🍃',
        'ice': '❄️',
        'fighting': '🥊',
        'poison': '☠️',
        'ground': '🌍',
        'flying': '🦅',
        'psychic': '🌀',
        'bug': '🐛',
        'rock': '🪨',
        'ghost': '👻',
        'dragon': '🐉',
        'dark': '🌑',
        'steel': '🛡️',
        'fairy': '🧚'
    }

    emoji = type_to_emoji.get(type_attack, '❓')  # Devuelve un emoji por defecto si el tipo no es reconocido
    return f"{name} {emoji}"