import os
import random
import time
from datetime import datetime

class WordScramble:
    def __init__(self, score_file='ws_scores.txt', match_history='match_history.txt'):
        self.score_file = score_file
        self.match_history = match_history
        self.word_list = ['python', 'hangman', 'programming', 'challenge', 'code', 'developer', 'computer', 'keyboard', 'software', 'hardware']

    def create_file(self):
        for file in [self.score_file, self.match_history]:
            if not os.path.exists(file):
                with open(file, 'w') as f:
                    pass
    
    def play_game(self, username):
        score = 0
        random.shuffle(self.word_list)

        start_time = time.time()
        for word in self.word_list:
            scrambled = ''.join(random.sample(word, len(word)))
            print(f'\nScrambled word: {scrambled}')
            
            guess_time_start = time.time()
            guess = input('Your guess: ').lower()
            guess_time_end = time.time()
            
            if guess_time_end - guess_time_start > 10:
                print('Time is up!')
                break
            
            if guess == word:
                print('Correct!')
                score += 1
            else:
                print(f'Incorrect! The word was {word}')

            if time.time() - start_time > 10:
                print('Time is up!')
                break

        end_time = time.time()
        total_time = end_time - start_time

        self.save_scores(username, score, total_time)
        self.save_match_history(username, score, total_time)
        print(f'Your score: {score} correct guesses in {total_time:.2f} seconds')


    def save_scores(self, username, score, total_time):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.score_file, 'a') as file:
            file.write(f'{username}: {score} correct guesses in {total_time:.2f} seconds on {now}\n')

    def save_match_history(self, username, score, total_time):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.match_history, 'a') as file:
            file.write(f'{username}: {score} correct guesses in {total_time:.2f} seconds on {now}\n')

