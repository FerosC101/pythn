from User import User

def main():
    print('WELCOME')
    user_instance = User("username", "password", "user_scores.txt", "User_Data")
    user_instance.menu()

if __name__ == '__main__':
    main()
