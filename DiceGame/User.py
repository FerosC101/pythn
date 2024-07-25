from Dice_game import dicegame
from User_Manager import UserManager

class User:
    def __init__(self, username, password, score_file, match_history_file):
        self.username = username
        self.password = password
        self.score_file = score_file
        self.match_history_file = match_history_file

    def register(self):
        print('Register to DR G!')
        username = input('Enter Username: ')
        password = input('Enter Password: ')
        password1 = input('Confirm Password: ')

        users = UserManager.load_users()

        while True:
            if password != password1:
                print('\n----- Password Doesnt match, Try again -----\n')
                self.register()
            elif not UserManager.validate_username(username, users) or not UserManager.validate_password(password):
                continue

            users[username] = (password, 0)
            UserManager.save_users(users)
            print('Success!\n')
            self.menu()
            break

    def login(self):
        users = UserManager.load_users()
        while True:
            username = input('Enter Username: ')
            password = input('Enter Password: ')
            
            if username in users and users[username][0] == password: 
                print('Login Successful!')
                self.game_menu(username)
                break  
            else:
                print('Incorrect username or password. Please try again.')


    def menu(self):
        print('\nWelcome to Dice Game! : )')
        print('1. Register')
        print('2. Log in')
        print('3. Exit')

        choice = input('Enter Choice: ')

        if choice == '1':
            self.register()
        elif choice == '2':
            self.login()
        elif choice == '3':
            quit()

    def game_menu(self, username):
        while True:
            print('\nWelcome to DR G!')
            print('1. Start Game')
            print('2. View Top Scores')
            print('3. Log out')

            choice = input('Enter Choice: ')
            if choice == '1':
                game_instance = dicegame(self.score_file, self.match_history_file)
                return_to_menu = game_instance.play_game(username) 
                if return_to_menu:
                    continue 
            elif choice == '2':
                game_instance = dicegame(self.score_file, self.match_history_file)
                game_instance.view_top_scores()
            elif choice == '3':
                self.menu()