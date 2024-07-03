from User_Management import User, UserManager
from Game_Logic import TicTacToe

class MainMenu:
    def __init__(self, user_manager):
        self.user_manager = user_manager
        self.current_user = None

    def display_menu(self):
        print('Welcome to Tic-Tac-Toe!')
        while True:
            print('1. Register')
            print('2. Log in')
            print('3. Exit')
            choice = input('Enter choice: ')
            if choice == '1':
                self.register()
            elif choice == '2':
                self.login()
            elif choice == '3':
                break

    def register(self):
        username = input('Enter username: ')
        password = input('Enter password: ')
        if self.user_manager.register(username, password):
            print('Registration successful!\n')
        else:
            print('Username already exists.\n')

    def login(self):
        username = input('Enter username: ')
        password = input('Enter password: ')
        if self.user_manager.login(username, password):
            print('Login successful!\n')
            self.current_user = username
            self.user_menu()
        else:
            print('Invalid username or password.\n')

    def user_menu(self):
        while True:
            print(f'\nWelcome {self.current_user}')
            print('1. Start a new game')
            print('2. View records')
            print('3. Log out')
            choice = input('Enter choice: ')
            if choice == '1':
                game = TicTacToe(self.current_user, self.user_manager)
                game.play_game()
            elif choice == '2':
                wins, losses = self.user_manager.get_user_record(self.current_user)
                print(f'Wins: {wins}, Losses: {losses}')
            elif choice == '3':
                self.current_user = None
                break

if __name__ == '__main__':
    user_manager = UserManager()
    main_menu = MainMenu(user_manager)
    main_menu.display_menu()