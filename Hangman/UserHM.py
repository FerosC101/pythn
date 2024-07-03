from UserManHM import User_Manager
from GameHM import Hangman
from ScoreHM import Score

class User:
    def __init__(self, username=None, password=None, score_file=None, match_history=None):
        self.username = username
        self.password = password
        self.score_file = score_file
        self.match_history = match_history

    def menu(self):
        while True:
            print('\nWelcome to Hangman :) ')
            print('1. Register')
            print('2. Login')
            print('3. Exit')


            choice = int(input('Enter Choice: '))
            if choice == 1:
                self.register()
            elif choice == 2:
                self.login()
            elif choice == 3:
                quit()
            else:
                print('Invalid Input')
          

    def register(self):
        username = input('Enter Username: ')
        password = input('Enter Password: ')

        users = User_Manager.load_users()

        while True:
            if not User_Manager.validate_name(users, username) or not User_Manager.validate_password(password):
                username = input('Enter Username: ')
                password = input('Enter Password: ')
                continue
                
            users[username] = password
            User_Manager.save_users(users)
            print('Success!\n')
            self.menu()
            break

    def login(self):
        users = User_Manager.load_users()
        while True:
            username = input('Enter Username: ')
            password = input('Enter Password: ')

            if username in users and users[username] == password:
                print('\nLog in successfully!\n')
                self.game_menu(username)
                break
            else:
                print('Invalid Username or Password, try again\n')

    def game_menu(self, username):
        game = Hangman()
        while True:
            print(f'\nWelcome {username}')
            print('1. Play Game')
            print('2. View Leaderboards')
            print('3. Log out')

            choice = int(input('Enter Choice: '))
            if choice == 1:
                game.play_game(username)
            elif choice == 2:
                Score.display_leaderboards()
            elif choice == 3: 
                self.menu()
            else:
                print('Invalid Choice')