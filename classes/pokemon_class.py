from logic.damage_calculation import damage


class Character:
    def __init__(self, name,attack,hp,defense, attacks, type):
        self.name = name
        self.__attack = attack
        self.__hp = hp + 300
        self.__defense = defense
        self.__attacks = attacks
        self.__type = type
    
    def attack(self):
        attk = self.__attack
        return attk
    
    def hp(self):
        hp = self.__hp
        return hp
    
    def defense(self):
        dfc = self.__defense
        return dfc
    
    def type_character(self):
        tp = self.__type
        return tp
    
    def show_info(self, enemy):
        data = 'HP    ATTK   DEF'
        self_data = f'{self.__hp}pts  {self.__attack}pts   {self.__defense}pts'
        enemy_data = ' ' * 32 + f'{enemy.hp()}pts  {enemy.attack()}pts   {enemy.defense()}pts'
        line = '_' * 23 + ' ' * 29 + '_' * 23
        
        print(f'{self.name.upper()}:' + ' ' * 50 + f'{enemy.name.upper()}:')
        print(line + f'\n  {data }' + ' ' * 36 + f'{data }\n{self_data}' + f'{enemy_data} \n' + line + '\n\n')
    
    def choose_attacks(self, enemy):
        count = 0
        self.show_info(enemy)
        print('Choose a attack')
        for move in self.__attacks:
            count += 1
            print(f"({count}) {move['name']}: Power: {move['power']}")
        try:   
            while True:
                chosen_attack = input('\nChosen attack: ').strip()
                if not chosen_attack or not chosen_attack.isdigit():
                    print('\ninvalid attack, please enter a number value\n')
                    continue
                chosen_attack = int(chosen_attack)
                if 1 <= chosen_attack <= len(self.__attacks):
                    chosen_attack -= 1
                    return self.use_attack(chosen_attack, enemy)
                else:
                    print('\nInvalid attack, enter a number within the range\n')
        except ValueError:
            print('Invalid attack')
            
    def use_attack(self,index, enemy):
        attack = self.__attacks[index]
        attack_type = attack['type']
        dmg = damage(self.__attack, attack, attack_type, enemy.defense(), enemy.type_character())
        print(f"{self.name.upper()} used {attack['name']}!")
        print(f"Attack Power: {attack['power']} | Type: {attack['type']}")
        print(f'relizo {dmg}pts de daño')
        enemy.receive_damage(dmg, enemy)
    
    def receive_damage(self, damage, enemy):
        self.__hp -= damage
        if self.__hp < 0:
            self.__hp = 0
        print(f'\n{self.name.upper()} RECEIVED {damage} DAMAGE\n')
        if not self.it_is_alive():
            print(f'{enemy.name} Esta muerto')
            
    def it_is_alive(self):
        alive = self.__hp
        if alive == 0:
            return False
        return True