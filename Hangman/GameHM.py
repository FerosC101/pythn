import random
import os
from datetime import datetime
import time

class Hangman:
    def __init__(self, score_file='hangman_scores.txt', match_history_file='Hangman_Match_History.txt'):
        self.score_file = score_file
        self.match_history_file = match_history_file
        self.create_files()
        self.word_list = ['python', 'hangman', 'programming', 'challenge', 'code']
        self.hangman_stages = [
            '''
             -----
             |   |
                 |
                 |
                 |
                 |
            ---------
            ''',
            '''
             -----
             |   |
             O   |
                 |
                 |
                 |
            ---------
            ''',
            '''
             -----
             |   |
             O   |
             |   |
                 |
                 |
            ---------
            ''',
            '''
             -----
             |   |
             O   |
            /|   |
                 |
                 |
            ---------
            ''',
            '''
             -----
             |   |
             O   |
            /|\  |
                 |
                 |
            ---------
            ''',
            '''
             -----
             |   |
             O   |
            /|\  |
            /    |
                 |
            ---------
            ''',
            '''
             -----
             |   |
             O   |
            /|\  |
            / \  |
                 |
            ---------
            '''
        ]

    def create_files(self):
        for file in [self.score_file, self.match_history_file]:
            if not os.path.exists(file):
                with open(file, 'w') as f:
                    pass

    def play_game(self, username):
        word = random.choice(self.word_list)
        guessed = '_' * len(word)
        attempts = 7
        guessed_letters = []

        start_time = time.time()

        while attempts > 0 and guessed != word:
            print(self.hangman_stages[7 - attempts])
            print(f'Word: {guessed}')
            print(f'Attempts left: {attempts}')
            print(f'Guessed letters: {", ".join(guessed_letters)}')
            guess = input('Enter a letter: ').lower()

            if guess in guessed_letters:
                print('You already guessed that letter.')
                continue

            guessed_letters.append(guess)

            if guess in word:
                guessed = ''.join([guess if word[i] == guess else guessed[i] for i in range(len(word))])
            else:
                attempts -= 1

            print('\n')

        end_time = time.time()
        elapsed_time = end_time - start_time

        if guessed == word:
            print(f'Congratulations! You guessed the word: {word}')
            score = elapsed_time
        else:
            print(self.hangman_stages[0])
            print(f'Game Over! The word was: {word}')
            score = elapsed_time

        self.save_scores(username, score)
        self.save_match_history(username, score, word)
        print(f'Your time: {score:.2f} seconds\n')

    def save_scores(self, username, score):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.score_file, 'a') as file:
            file.write(f'{username}: {score:.2f} seconds on {now}\n')
        
    def save_match_history(self, username, score, word):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.match_history_file, 'a') as file:
            file.write(f'{username}: {score:.2f} seconds for word "{word}" on {now}\n')
