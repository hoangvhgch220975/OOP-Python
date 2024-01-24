from math import atan
import random
import stat

n_wins = 0
n_loses = 0
n_ties = 0
choices = ['rock', 'paper', 'scissor']

def play_game():
    n_wins = 0
    n_loses = 0
    n_ties = 0
    n_turns = 5
    for i in range(1,n_turns+1):
        print(f'Turn {i}')
        comp_choice = computer_choose()
        player_choice = player_choose()
        status = compare(comp_choice, player_choice)
        n_wins+=1 if status == 1 else 0
        n_loses+=1 if status == -1 else 0
        n_ties+=1 if status == 0 else 0

    print(f'Player win: {n_wins}')
    print(f'Computer win: {n_loses}')
    print(f'Tie: {n_ties}')

def computer_choose():
    return random.choice(choices)

def player_choose():
    choice = input('Enter your choice (rock, paper, scissor): ')
    while choice not in choices:
        print('Invalid choice. Please try again')
        choice = input('Enter your choice (rock, paper, scissor): ')
    return choice

def compare(comp_choice, player_choice):
    print(f'Player : {player_choice},  Computer: {comp_choice}')
    if comp_choice == player_choice:
        print('Tie!')
        return 0
    elif player_choice =='rock' and comp_choice == 'scissor' or\
    player_choice =='paper ' and comp_choice == 'rock' or\
    player_choice == 'scissor' and comp_choice == 'paper':
        print('Player win!')
        return 1
    else:
        print('Computer wwin!')
        return -1

play_game()