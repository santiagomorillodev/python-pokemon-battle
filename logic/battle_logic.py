import random
def battle(player_1, player_2):

    print('May the battle begin!')
    turn = random.randint(1, 2)

    if turn == 1:
        player_1.choose_attacks(player_2)
        print('Turno de player 2')
        player_2.choose_attacks(player_1)
        turn = 1
    else:
        player_2.choose_attacks(player_1)
        print('Turno de player 2')
        player_1.choose_attacks(player_2)
        turn = 2
        
    while player_1.it_is_alive() and player_2.it_is_alive():
        if turn == 1:
            if player_1.it_is_alive():
                player_1.choose_attacks(player_2)
                turn = 2
        if turn == 2:
            if player_2.it_is_alive():
                player_2.choose_attacks(player_1)
                turn = 1
    
    if player_1.it_is_alive():
        print('Player 1 WIND!!')
    else:
        print('Player 1 WIND!!')
    