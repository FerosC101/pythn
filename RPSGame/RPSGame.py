import os
import random
from datetime import datetime

class RockPaperScissor:
    def __init__(self, score_file='rps_scores.txt', match_histor_file='RPS_Match_History.txt'):
        self.score_file = score_file
        self.match_history_file = match_histor_file
        self.create_files()
        
    def create_files(self):
        for file in [self.score_file, self.match_history_file]:
            if not os.path.exists(file):
                with open(file, 'w') as f:
                    pass
    
    def play_game(self, username):
        moves = ['rock', 'paper', 'scissors']
        user_score = 0
        computer_score = 0

        for x in range(10):
            user_move = input('Enter your move (rock, paper, scissors): ').lower()
            if user_move not in moves:
                print('Invalid move! Try again.\n')
                continue

            computer_move = random.choice(moves)
            print(f'computer move: {computer_move}')

            if user_move == computer_move:
                print('It\'s a tie!')
            elif (user_move == 'rock' and computer_move == 'scissors') or \
                (user_move == 'paper' and computer_move == 'rock') or \
                (user_move == 'scissors' and computer_move == 'paper'):
                print('\nYou win this round!')
                user_score += 1
            else:
                print('\nComputer wins this round!')
                computer_score += 1

            print(f'Score: You {user_score} - {computer_score} Computer\n')

        if user_score > computer_score:
            print('Congratulations! You won the game.')
        else:
            print('Computer wins the game. Better luck next time!')

        self.save_scores(username, user_score)
        self.save_match_history(username, user_score, computer_score)

    def save_scores(self, username, score):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.score_file, 'a') as file:
            file.write(f'{username}: {score} wins on {now}\n')

    def save_match_history(self, username, user_score, computer_score):
        now = datetime.now().strftime('%Y-%m-%d %H:%M-%S')
        with open(self.match_history_file, 'a') as file:
            file.write(f'{username}: {user_score} vs Computer: {computer_score} on {now}\n')