
import random

class Player:
    def __init__(self):
        self.wins = 0
    def choose(self):
        choices = ['rock', 'paper', 'scissor']
        choice = input('Enter your choice (rock, paper, scissor): ')
        while choice not in choices:
            print('Invalid choice. Please try again')
            choice = input('Enter your choice (rock, paper, scissor): ')
        return choice
    
class Computer:
    def __init__(self):
        self.wins = 0
    def choose(self):
        choices = ['rock', 'paper', 'scissor']
        return random.choice(choices)
    
class Game:
    def __init__(self,turns):
        self.player = Player()
        self.computer = Computer()
        self.n_turn = turns 
    def play(self):
        for i in range(1,self.n_turn+1):
            print(f'Turn {i}')
            comp_choice = self.computer.choose()
            player_choice = self.player.choose()
            status = self.compare(comp_choice, player_choice)

            self.player.wins += 1 if status == 1 else 0
            self.computer.wins +=1 if status == -1 else 0
        print(f'Player win: {self.player.wins}')
        print(f'Computer win: {self.computer.wins}')
        print(f'Tie: {self.n_turn - self.player.wins - self.computer.wins}')
    def compare(self, comp_choice, player_choice):
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
# Main       
game = Game(5)
game.play()



