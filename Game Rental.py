games_lib = {
    'Donkey kong': {'quantity': 3, 'cost': 2},
    'Super Mario': {'quantity': 5, 'cost': 3},
    'Tetris': {'quantity': 2, 'cost': 1},
}

user_acc = {}

user_inventory = {}

admin_user = 'admin'
admin_password = 'adminpass'

def main_menu():
    print('Welcome to Game rental System!')
    print('1. Available Games')
    print('2. Register')
    print('3. Admin Log-in')
    print('4. User Log-in')
    print('5. Exit\n')

    choice = int(input('Choose an option: '))

    if choice == 1:
        display_available_games()
    if choice == 2:
        register()
    if choice == 3:
        admin_login()
    if choice == 4:
        user_login()
    if choice == 5:
        print('Thank you!')
        quit()


def display_available_games():
    print([games_lib])
    print()
    choice = input('Return to Main Menu (press y): ')
    if choice.lower() == 'y':
        main_menu()
    
def register():
    print('Register to access and rents games : )')
    username = input('Enter Username: ')
    password = input('Enter Passoword: ')
    balance = 0
    points = 0

    user_acc[username] = {
        'username' : username ,
        'password' : password,
        'balance' : balance,
        'points' : points
    }

    while len(password) < 8:
        print('password must at least have the minimum of 8 characters')
        password = input('Enter Password: ')

    print()
    print(f'Your username is {username} and your password is {password}, your current balance is {balance} and your current points is{points}')
    print('Welcome!\n')

    choice = int(input('Do you wish to Log in(2) or Return to Main Menu?(1): '))
    if choice == 1:
        main_menu()
    if choice == 2:
        user_login()
    if choice != 1 or 2:
        print('Invalid Input!')
        choice = int(input(print('Do you wish to Log in(2) or Return to Main Menu?(1): ')))

def admin_login():
    while True:
        username = input('Enter Admin User: ')
        password = input('Enter Admin Passowrd: ')

        if username == admin_user and password == admin_password:
            admin_menu()
            break
        else:
            print('Invalid Username or Password\n')


def user_login():
    username = input("Username: ")
    password = input("Password: ")
    if username in user_acc and user_acc[username]['password'] == password:
        print(f'Welcome {username}')
        user_menu(username)
    else: 
        print ("wrong username or password")
        main_menu()


def admin_menu():
    print('Welcom Admin')
    print('1. Update Library')
    print('2. Exit\n')

    while True:
        choice = int(input('Enter Choice: '))

        if choice == 1:
            admin_edit()
            break
        if choice == 2:
            main_menu()
            break

def admin_edit():
        print(games_lib)
        print()
        print('1. Edit price')
        print('2. Edit Quantity')
        print('3. Add New Games')
        print('4. Log out')
        choice = int(input('Enter choice: '))

        if choice == 1:
            game_name = input('Enter the name of the game whose price you want to edit: ')
            if game_name in games_lib:
                new_price = int(input('Enter the new price: '))
                games_lib[game_name]['cost'] = new_price
                print('Price updated successfully!')
                admin_edit()
            else:
                print('Game not found in the library.')
                admin_edit()
        elif choice == 2:
            game_name = input('Enter the name of the game whose quantity you want to edit: ')
            if game_name in games_lib:
                new_quantity = int(input('Enter the new quantity: '))
                games_lib[game_name]['quantity'] = new_quantity
                print('Quantity updated successfully!')
                admin_edit()
            else:
                print('Game not found in the library.')
                admin_edit()
        elif choice == 3:
            add_new_game()
        elif choice == 4:
            main_menu()
        else:
            print('Invalid choice.')
            admin_edit()

def add_new_game():
    print('\nAdd New Game!')
    game_name = input("Enter the name of the new game: ")
    quantity = int(input("Enter the quantity available: "))
    cost = int(input("Enter the cost to rent the game: "))
    games_lib[game_name] = {'quantity': quantity, 'cost': cost}
    print(f"Game '{game_name}' added successfully!\n")

    choice = input('Enter y to return to admin menu: ')
    if choice.lower() == 'y':
        admin_edit()

def user_menu(username):
    print('Welcome to Game Rental')
    print('1. Rent a game')
    print('2. Return a game')
    print('3. Top up')
    print('4. Check Inventory')
    print('5. Redeem Points')
    print('6. Check points')
    print('7. Exit\n')

    choice = int(input('Enter Choice: '))

    if choice == 1:
        rent_game(username)
    elif choice == 2:
        return_game(username)
    elif choice == 3:
        top_up(username)
    elif choice == 4:
        check_inventory(username)
    elif choice == 5:
        redeem_points(username)
    elif choice == 6:
        check_points(username)
    elif choice == 7:
        main_menu()

def rent_game(username):
    while True:
        try:
            print('Rent a game')
            print(games_lib)

            gamename = input('Select Game by typing the game name: ')

            if gamename in games_lib and games_lib[gamename]['quantity'] > 0:
                if user_acc[username]['balance'] >= games_lib[gamename]['cost']:
                    user_acc[username]['balance'] -= games_lib[gamename]['cost']
                    games_lib[gamename]['quantity'] -= 1
                    user_acc[username]['points'] += 1
                    if username not in user_inventory:
                        user_inventory[username] = [gamename]
                    else:
                        user_inventory[username].append(gamename)
                    print(f'Game Successfully rented, Remaining balance is: {user_acc[username]["balance"]}\n')
                else:
                    print('Insufficient Balance')
            elif gamename in games_lib and games_lib[gamename]['quantity'] <= 0:
                print('Game is out of stock')
            else:
                print('Invalid game selection')

        except ValueError as e:
            user_menu(username)

        choice = input('Enter A to rent another game, enter Y to return to menu: ')
        if choice.lower() == 'y':
            return user_menu(username)
        elif choice.lower() != 'a':
            print('Invalid Input. Enter A or Y only')


def return_game(username):
    while True:
        try:
            print("\nReturn a game")
            print(user_inventory[username])

            game_name = input("\nEnter the name of the game to return: ")
            
            if game_name in user_inventory.get(username, []):
                user_inventory[username].remove(game_name)
                games_lib[game_name]['quantity'] += 1
                print(f"Game '{game_name}' returned successfully.\n")
            else:
                print("Game not found in the user's inventory or not rented by the user.\n")

        except ValueError as e:
            user_menu(username)
        
        choice = input('Press Y to return to the main menu: ')
        if choice.lower() == 'y':
            return user_menu(username)

def top_up(username):
    while True:
        try:
            amount = int(input('Enter Amount to Top up: '))

            user_acc[username]['balance'] += amount
            print(f'You have deposited {amount}, your new balance is {user_acc[username]["balance"]}\n')
        
        except ValueError as e:
            user_menu(username)

        choice = input('Enter y to return to menu: ')
        if choice.lower() == 'y':
            user_menu(username)
    

def check_inventory(username):
    while True:
        try:
            print()
            if username in user_inventory:
                print(f'Your inventory: {user_inventory[username]}\n')
            else:
                print("Your inventory is empty.\n")

        except ValueError as e:
            user_menu(username)

        choice = input('Press y to return to the main menu: ')
        if choice.lower() == 'y':
            return user_menu(username)

def redeem_points(username):
    while True:
        try:
            print()
            print('Redeem Points\n')
            
            if user_acc[username]["points"] >= 3:
                print("You can redeem your points to rent a game.")
                choice = input("Do you want to redeem points? (Y/N): ")
                if choice.lower() == "y":
                    user_acc[username]["points"] -= 3
                    print("Points redeemed successfully!")
                    print(games_lib)
                    gamename = input("Select a game by typing the game name: ")
                    if gamename in games_lib and games_lib[gamename]['quantity'] > 0:
                        games_lib[gamename]['quantity'] -= 1
                        user_inventory[username] = user_inventory.get(username, []) + [gamename]
                        print(f'Game "{gamename}" successfully rented!\n')
                        return user_menu(username)
                    else:
                        print('Invalid game selection or game is out of stock')
                        redeem_points(username)
                elif choice == "n":
                    user_menu(username)
                else:
                    print("Invalid input. Please enter Y or N.")
                    redeem_points(username)
            else:
                print("You do not have enough points to redeem.")
                redeem_points(username)
        except ValueError as e:
            user_menu(username)


def check_points(username):
    print(f'Available points: {user_acc[username]["points"]}\n')
    print('Enter Choice')
    print('1. Redeem points')
    print('2. Exit')
    choice = input('Enter choice: ')
    if choice == '1':
        redeem_points(username)
    elif choice == '2':
        return user_menu(username)


main_menu()
