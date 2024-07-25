from UserManTST import UserManager
from GameLogicTST import TypingSpeedTest

class MainMenu:
    def __init__(self):
        self.user_manager = UserManager()
        self.current_user = None
        self.typing_test = TypingSpeedTest()

    def run(self):
        while True:
            print("\n1. Register\n2. Log In\n3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.register()
            elif choice == "2":
                self.login()
                if self.current_user:
                    self.main_menu()
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")

    def register(self):
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        if self.user_manager.register_user(username, password):
            print("User registered successfully.")
        else:
            print("Username already taken.")

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        self.current_user = self.user_manager.login_user(username, password)
        if self.current_user:
            print("Login successful.")
        else:
            print("Invalid username or password.")

    def main_menu(self):
        while True:
            print("\n1. Start Typing Test\n2. View High Scores\n3. Log Out")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.select_typing_test()
            elif choice == "2":
                self.view_high_scores()
            elif choice == "3":
                self.current_user = None
                break
            else:
                print("Invalid choice. Please try again.")

    def select_typing_test(self):
        print("\n1. Typing Test by Time\n2. Typing Test by Words")
        choice = input("Enter your choice: ")
        if choice == "1":
            self.typing_test_by_time()
        elif choice == "2":
            self.typing_test_by_words()
        else:
            print("Invalid choice. Please try again.")

    def typing_test_by_time(self):
        print("\nSelect duration:")
        print("1. 15 seconds\n2. 30 seconds\n3. 60 seconds")
        choice = input("Enter your choice: ")
        if choice == "1":
            self.typing_test.start_typing_test(self.current_user, 'time', 15)
        elif choice == "2":
            self.typing_test.start_typing_test(self.current_user, 'time', 30)
        elif choice == "3":
            self.typing_test.start_typing_test(self.current_user, 'time', 60)
        else:
            print("Invalid choice. Please try again.")

    def typing_test_by_words(self):
        print("\nSelect word count:")
        print("1. 10 words\n2. 20 words\n3. 50 words")
        choice = input("Enter your choice: ")
        if choice == "1":
            self.typing_test.start_typing_test(self.current_user, 'words', 10)
        elif choice == "2":
            self.typing_test.start_typing_test(self.current_user, 'words', 20)
        elif choice == "3":
            self.typing_test.start_typing_test(self.current_user, 'words', 50)
        else:
            print("Invalid choice. Please try again.")

    def view_high_scores(self):
        if not self.current_user.high_scores:
            print("No high scores yet.")
        else:
            print("High Scores:")
            for idx, score in enumerate(self.current_user.high_scores, start=1):
                print(f"{idx}. {score:.2f} WPM")



if __name__ == "__main__":
    menu = MainMenu()
    menu.run()