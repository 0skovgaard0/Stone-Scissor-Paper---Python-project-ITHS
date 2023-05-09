# This Python code is a simple text-based game of Stone, Scissor, Paper. 
The game is played between a human player and a computer player represented by Arnold Schwarzenegger. The first player to win 3 rounds wins the game. The game prompts the user for their choice of stone, scissor, or paper and compares it with the computer's randomly generated choice.

### Game Rules:

Stone beats Scissor
Scissor beats Paper
Paper beats Stone

### Classes:

Player: A base class representing a generic player, which has attributes like name, score, and choice, and a choose() method, which will be overridden in child classes.
HumanPlayer: A subclass of Player, represents the human player, and overrides the choose() method to take input from the user.
ComputerPlayer: A subclass of Player, represents the computer player, and overrides the choose() method to generate a random choice.

### Functions:

play_game(player1, player2): The main game logic is contained in this function. It compares the choices of both players and updates their scores accordingly. The game continues until one of the players wins 3 rounds.

### How to run the game:

Save the provided code in a Python file, e.g., stone_scissor_paper.py.
Open a terminal or command prompt and navigate to the directory containing the file.
Run the command python stone_scissor_paper.py.
Follow the on-screen prompts to enter your name and your choices in each round.

Enjoy the game!