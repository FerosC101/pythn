import random
import os
from datetime import datetime

class NumberGuessingGame:
    def __init__(self, easy_score_file='easy_scores.txt', medium_score_file='medium_scores.txt', hard_score_file='hard_scores.txt', match_history_file='Match_Score.txt'):
        self.easy_score_file = easy_score_file
        self.medium_score_file = medium_score_file
        self.hard_score_file = hard_score_file
        self.match_history_file = match_history_file
        self.create_files()

    def create_files(self):
        for file in [self.easy_score_file, self.medium_score_file, self.hard_score_file, self.match_history_file]:
            if not os.path.exists(file):
                with open(file, 'w') as f:
                    pass

    def play_game(self, username):
        print('\nChoose level')
        print('1. Easy (1-10)')
        print('2. Medium (1-50)')
        print('3. Hard (1-100)')

        while True:
            choice = int(input('Enter Choice: '))
            if choice == 1:
                random_number = random.randint(1, 10)
                score_file = self.easy_score_file
                level = 'Easy'
            elif choice == 2:
                random_number = random.randint(1, 50)
                score_file = self.medium_score_file
                level = 'Medium'
            elif choice == 3:
                random_number = random.randint(1, 100)
                score_file = self.hard_score_file
                level = 'Hard'
            else:
                print('Invalid choice, try again.\n')
                continue

            print()
            guess = 0

            while True:
                guess += 1
                number = input('Enter Number: ')
                if number.isdigit():
                    number = int(number)
                else:
                    print('Enter a valid number\n')
                    continue

                if number > random_number:
                    print('Go lower!\n')
                elif number < random_number:
                    print('Go higher!\n')
                else:
                    print(f'Congratulations\nYou guessed {guess} times')
                    self.save_scores(username, guess, score_file)
                    self.save_match_history(username, guess, level)
                    break
            break

    def save_scores(self, username, score, score_file):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(score_file, 'a') as file:
            file.write(f'{username}: {score} attempts on {now}\n')
        
    def save_match_history(self, username, score, level):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.match_history_file, 'a') as file:
            file.write(f'{username}: {score} on level {level} at {now}\n')
