import random
import time

# Game rules
print(''' Remember the game rules:
    Stone > Scissor
    Scissor > Paper
    Paper > Stone

    The one who wins 3 rounds = Wins!
    ''')

class Player: 
    # class Player works as the base class, common attributes and
    # methods for both HumanPlayer and ComputerPlayer
    def __init__(self, name):
        # name stores the name of players, score stores the players score
        # choice stores players choice; Stone, Scissor or Paper
        self.name = name
        self.score = 0
        self.choice = None

    def choose(self):
        pass

    def __str__(self):
        # returns the players names and display in the game output
        return self.name
    
class HumanPlayer(Player):
    def choose(self):
        # overides choose method to take input from the user
        choice = input('Write your choice: Stone, Scissor or Paper: ').lower()
        while choice not in ['stone', 'scissor', 'paper']:
            print(f'''Dear {self.name}, Me Arnold Schwarzenegger - No brain, only MUCLES, 
            please check your spelling: "Stone", "Scissor", "Paper".''')
            choice = input('Write your choice: Stone, Scissor or Paper: ').lower()
        self.choice = choice

class ComputerPlayer(Player):
    # overides choose method to generate a random choice
    def choose(self):
        self.choice = random.choice(['stone', 'scissor', 'paper'])

def play_game(player1, player2):
    # Game continues until one player wins three times
    # game logic represent within this func
    while player1.score < 3 and player2.score < 3:
        player1.choose()
        player2.choose()

        print(f'{player1} chose {player1.choice}.')
        print(f'{player2} chose {player2.choice}.')

        if player1.choice == player2.choice:
            print(f'Tie! both chose {player1.choice}!')
        elif (player1.choice == 'stone' and player2.choice == 'scissor') or \
             (player1.choice == 'scissor' and player2.choice == 'paper') or \
             (player1.choice == 'paper' and player2.choice == 'stone'):
            print(f'{player1} wins this round!')
            player1.score += 1
        else:
            print(f'{player2} wins this round!')
            player2.score += 1

        print(f'The current score is {player1.score} - {player2.score}.\nNext round, lets go!')
        print('-'*25)
    
    if player1.score == 3:
        print(f'{player1} has won the game! And {player2} has to take 100 pushups!')
        time.sleep(1)
        print(f'{player2} "I will be BACK!"')
    else:
        print(f'{player2} has won the game!')

# Initialize the players
player_name = input('Welcome to the game of Stone, Scissor, Paper. Please enter a player name and hit enter: ')
p1 = HumanPlayer(player_name)
p2 = ComputerPlayer('Arnold Schwarzenegger')

# Start the game
play_game(p1, p2)
