from colorama import init, Fore, Style
import time

market = {
    'Bags': {
        'Gucci': {'stock': 10, 'price': 700},
        'Louis Vuitton': {'stock': 8, 'price': 850},
        'Prada': {'stock': 8, 'price': 700}
    },
    'Shoes': {
        'Nike': {'stock': 15, 'price': 400},
        'Adidas': {'stock': 10, 'price': 250},
        'Converse': {'stock': 9, 'price': 230},
    },
    'Clothes': {
        'Saint Laurent': {'stock': 20, 'price': 500},
        'Fendi': {'stock': 25, 'price': 200},
        'Valentino': {'stock': 20, 'price': 400}
    }
}

user_acc = {}
basket = {}

admin_user = 'admin'
admin_password = 'password'

def text_appear_Time(message, delay):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(delay)

def home_page():
    text_appear_Time('\nWelcome to Market Place!\n', 0.04)
    print('1. Sign-up')
    print('2. Log-in')
    print('3. Admin Log-in')
    print('4. How to use app')
    print('5. Exit\n')

    while True:
        choice = input('Enter Choice: ')
        if choice == '1':
            sign_up()
            break
        elif choice == '2':
            user_login()
            break
        elif choice == '3':
            admin_login()
            break
        elif choice == '4':
            directions()
            break
        elif choice == '5':
            quit()
        else:
            print('Invalid Input!')

def sign_up():
    print('\nSign up to Enter\n')
    username = input('Enter username: ')
    password = input('Enter password: ')
    money = 0
    points = 0

    user_acc[username] = {
        'username': username,
        'password': password,
        'money': money,
        'points': points,
    }

    while len(password) < 8:
        print('Password must be at least 8 characters long.')
        password = input('Enter Password: ')

    print(f'\nYour username is {username} and your password is {password}. Your current balance is {money} and your current points is {points}.')
    print('Welcome!\n')

    choice = input('Do you wish to Log in(2) or Return to Main Menu(1): ')
    if choice == '1':
        home_page()
    elif choice == '2':
        user_login()
    else:
        print('Invalid Input!')
        sign_up()

def user_login():
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if not (username and password):
        print("\nUsername or password cannot be empty.\n")
        user_login()
    elif username in user_acc and user_acc[username]['password'] == password:
        marketplace(username)
    else:
        print("\nInvalid username or password.\n")
        user_login()

    print(f'Welcome, {username}!')

def admin_login():
    while True:
        username = input('Enter Admin User: ')
        password = input('Enter Admin Password: ')

        if username == admin_user and password == admin_password:
            admin_menu()
            break
        else:
            print('Invalid Username or Password\n')

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
            home_page()
            break
        else:
            admin_menu()

def admin_edit():
    print('ADMIN CONTROLL')
    print()
    print('1. Edit price')
    print('2. Edit Quantity')
    print('3. Add New Product')
    print('4. Add New Brand')
    print('5. Log out')

    choice = int(input('Enter choice: '))
    if choice == 1:
        category = input('Enter Category: ').capitalize()
        if category in market:
            brand = input('Enter Brand: ').capitalize()
            if brand in market[category]:
                while True:
                    try:
                        new_price = int(input('Enter new price: '))
                        market[category][brand]['price'] = new_price
                        print(f'Price of {market[category]} Successfully updated\n')
                        admin_edit()
                        break
                    except ValueError:
                        print('Invalid input! Please enter a valid price.')
            else:
                print('Brand not found in market\n')
        else:
            print('Category not found\n')
    elif choice == 2:
        category = input('Enter Category: ').capitalize()
        if category in market:
            brand = input('Enter Brand: ').capitalize()
            if brand in market[category]:
                while True:
                    try:
                        new_stocks = int(input('Enter new quantity: '))
                        market[category][brand]['stock'] = new_stocks
                        print(f'Quantity of {market[category]} Successfully updated\n')
                        admin_edit()
                        break
                    except ValueError:
                        print('Invalid input! Please enter a valid quantity.')
            else:
                print('Brand not found in market\n')
                admin_edit()
        else:
            print('Category not found\n')
            admin_edit()
    elif choice == 3:
        new_product = input('Enter new product: ').capitalize()
        if new_product not in market:
            brand = ''
            stock = 0
            price = 0
            market[new_product] = {'brand': brand, 'stocks': stock, 'price': price}
            print(f'{new_product} was added successfully to products\n')
            return admin_edit()
        else:
            print('Product already exists\n')
    elif choice == 4:
        category = input('Enter Category: ').capitalize()
        if category in market:
            new_brand = input('Enter new brand: ').capitalize()
            if new_brand not in market[category]:
                while True:
                    try:
                        quantity = int(input('Enter how many to add: '))
                        price = int(input('Enter New product price: '))

                        market[category][new_brand] = {'stock': quantity, 'price': price}
                        print(f'{new_brand} was added successfully to {category}\n')
                        return admin_edit()
                    except ValueError:
                        print('Invalid input! Please enter valid quantity and price.')
            else:
                print('Brand already exists in the category\n')
                admin_edit()
        else:
            print('Category not found\n')
            admin_edit()
    elif choice == 5:
        home_page()
    else:
        print('Invalid Input\n')
        admin_edit()

def directions():
    text_appear_Time('Hello and welcome! My name is Vince, and I will be your tutorial guide today.\n', 0.1)
    text_appear_Time('How may I assist you today?\n', 0.1)

    print('\n1. Logging in')
    print('2. Buying')
    print('3. Checking out basket')
    print('4. Money Transfer')
    print('5. Points system')
    print('6. Exit')

    choice = input('Enter Choice: ')
    if choice == '1':
        print()
        text_appear_Time('In order to log in, you must sign-up first with your username and password by pressing "1". Remember that the password length must be 8 characters or more!\n', 0.05)
    elif choice == 2:
        print()
        text_appear_Time('In order to purchase, you must enter the category one by one, first enter the Category then the brand and the quantity and it will automatically go to your basket\n', 0.05)
    elif choice == 3:
        print()
        text_appear_Time('After Adding products to your basket, you can edit your basket to remove an item and after that you can check out all of your items\n', 0.05)
    elif choice == 4:
        print()
        text_appear_Time('If you have no balance, you can go to bank for a money transfer which you can use for paying\n', 0.05)
    elif choice == 5:
        print()
        text_appear_Time('For every $1 you will receive a 0.12 amount of points where you can also use for paying\n', 0.05)
    elif choice == 6:
        home_page
    else:
        print('Invalid Input')
        directions()

def marketplace(username):
    print('\nWelcome! Purchase whatever you need.')
    print('1. Display Available Products')
    print('2. Shop now')
    print('3. Check out basket')
    print('4. Go to bank')
    print('5. Check and Redeem points')
    print('6. Log-out')

    choice = input('Enter choice: ')
    if choice == '1':
        display_market(username)
    elif choice == '2':
        shop_now(username)
    elif choice == '3':
        checkout(username)
    elif choice == '4':
        bank(username)
    elif choice == '5':
        redeem_and_check_points(username)
    elif choice == '6':
        home_page()
    else:
        print('Invalid Input')
        marketplace(username)

def display_market(username):
    print("\nAvailable Products:")
    for category, brands in market.items():
        print(f'\n{category}: ')
        for brand, details in brands.items():
            print(f'\t{brand}:')
            print(f'\t\tStock: {details["stock"]}')
            print(f'\t\tPrice: ${details["price"]}')

    choice = input('Enter SHOP to go to store or Enter BACK to return to menu: ')
    if choice.upper() == 'SHOP':
        shop_now(username)
    elif choice.upper() == 'BACK':
        marketplace(username)
    else:
        print('Invalid choice.')
        display_market(username)

def shop_now(username):
    text_appear_Time('\nWelcome to the store!\n', 0.04)
    print()
    for category, brands in market.items():
        print(f'\n{category}: ')
        for brand, details in brands.items():
            print(f'\t{brand}:')
            print(f'\t\tStock: {details["stock"]}')
            print(f'\t\tPrice: ${details["price"]}')
    category_choice = input('\nEnter the category you want to shop from (Bags/Shoes/Clothes): ').capitalize()
    if category_choice in market:
        brand_choice = input(f'Enter the brand you want to shop from {category_choice}: ').capitalize()
        if brand_choice in market[category_choice]:
            while True:
                try:
                    quantity = int(input('Enter the quantity you want to buy: '))
                    if 0 < quantity <= market[category_choice][brand_choice]['stock']:
                        if username in basket:
                            if category_choice in basket[username]:
                                if brand_choice in basket[username][category_choice]:
                                    basket[username][category_choice][brand_choice] += quantity
                                else:
                                    basket[username][category_choice][brand_choice] = quantity
                            else:
                                basket[username][category_choice] = {brand_choice: quantity}
                        else:
                            basket[username] = {category_choice: {brand_choice: quantity}}
                        print(f'\n{quantity} {brand_choice} {category_choice} added to your basket.')
                        break
                    else:
                        print('Invalid quantity or not enough stock.')
                except ValueError:
                    print('Invalid input! Please enter a valid quantity.')
        else:
            print('Invalid brand choice.')
    else:
        print('Invalid category choice.')

    choice = input("\nEnter MORE to continue shopping or Enter CHECKOUT to proceed to checkout and Enter BACK to exit: ")
    if choice.upper() == 'MORE':
        shop_now(username)
    elif choice.upper() == 'CHECKOUT':
        checkout(username)
    elif choice.upper() == 'BACK':
        marketplace(username)
    else:
        print('Invalid choice.')
        shop_now(username)

def checkout(username):
    total_price = 0
    print("\nYour Basket:")
    if username in basket:
        for category, brands in basket[username].items():
            for brand, quantity in brands.items():
                price_per_item = market[category][brand]['price']
                total_price += price_per_item * quantity
                print(f"{quantity} {brand} {category} - Price: {price_per_item * quantity}")

        print(f"\nTotal Price: {total_price}")
        while True:
            choice = input("Would you like to edit your basket? (yes/no): ").strip().lower()
            if choice == "yes":
                edit_basket(username)
                break
            elif choice == "no":
                confirm = input("Confirm checkout (yes/no): ").strip().lower()
                if confirm == 'yes':
                    if total_price <= user_acc[username]['money']:
                        user_acc[username]['money'] -= total_price
                        user_points = float(total_price * 0.12)
                        user_acc[username]['points'] += user_points
                        for category, brands in basket[username].items():
                            for brand, quantity in brands.items():
                                market[category][brand]['stock'] -= quantity
                        del basket[username]
                        print('Checkout successful!')
                        break
                    else:
                        print('Insufficient Money to Checkout')
                elif confirm == "no":
                    print('Checkout canceled.')
                    break
                else:
                    print("Invalid choice. Please enter 'yes' or 'no'.")
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")
    else:
        print('Your basket is empty.')
    
    choice = input('Enter BACK to go back to menu: ')
    if choice.upper() == 'BACK':
        marketplace(username)
    else:
        print('Invalid Input')
        checkout(username)

def edit_basket(username):
    print("\nEdit Basket:")
    if username in basket:
        for category, brands in basket[username].items():
            for brand, quantity in brands.items():
                print(f"{quantity} {brand} {category}")
        while True:
            category_choice = input("Enter the category you want to edit: ").capitalize()
            brand_choice = input("Enter the brand you want to remove: ").capitalize()
            if category_choice in basket[username] and brand_choice in basket[username][category_choice]:
                while True:
                    try:
                        quantity_to_remove = int(input("Enter the quantity to remove: "))
                        if quantity_to_remove <= basket[username][category_choice][brand_choice]:
                            basket[username][category_choice][brand_choice] -= quantity_to_remove
                            if basket[username][category_choice][brand_choice] == 0:
                                del basket[username][category_choice][brand_choice]
                                if not basket[username][category_choice]:
                                    del basket[username][category_choice]
                            print("Item(s) removed from basket.")
                            break
                        else:
                            print("Invalid quantity. Please enter a valid quantity to remove.")
                    except ValueError:
                        print("Invalid input! Please enter a valid quantity.")
                break
            else:
                print("Invalid category or brand choice. Please enter valid choices.")
    else:
        print('Your basket is empty.')


def bank(username):
    print('Loading')
    text_appear_Time('...', 0.5)
    print()
    print('Welcome to the bank\n')
    print(f'Your current balance is: {user_acc[username]["money"]}\n')
    print('1. Withdraw Cash')
    print('2. Exit\n')

    choice = input('Enter Choice: ')
    if choice == '1':
        while True:
            try:
                amount = int(input('Enter amount to withdraw: '))
                user_acc[username]['money'] += amount
                print(f'You have deposited ${amount}, your new balance is ${user_acc[username]["money"]}\n')
                while True:
                    choice = input('Enter BACK to return to menu: ')
                    if choice.upper() == 'BACK':
                        marketplace(username)
                        break
                break
            except ValueError:
                print('Invalid input! Please enter a valid amount.')
    elif choice == '2':
        marketplace(username)
    else:
        print('\nInvalid Input\n')
        bank(username)

def redeem_and_check_points(username):
    while True:
        try:
            print(f'Your current points is: {user_acc[username]["points"]}\n')
            choice = input('Enter REDEEM to redeem your points and RETURN to go back: ')
            if choice.upper() == 'REDEEM':
                category_choice = input('Enter Category: ')
                if category_choice in market:
                    brand_choice = input('Enter brand: ')
                    if brand_choice in market[category_choice]:
                        if market[category_choice][brand_choice]['stock'] > 0:
                            price = market[category_choice][brand_choice]['price']
                            points_deducted = float(price) * 0.12
                            if user_acc[username]["points"] >= points_deducted:
                                user_acc[username]["points"] -= points_deducted
                                market[category_choice][brand_choice]['stock'] -= 1
                                print('Redeemed successfully!')
                                break
                            else:
                                print('Insufficient points to redeem.')
                        else:
                            print('Out of stock')
                    else:
                        print('Brand not in category')
                else:
                    print('Category not in Market')
            elif choice.upper() == 'RETURN':
                marketplace(username)
                break
            else:
                print('Invalid Input')
        except ValueError:
            print('Invalid input! Please enter a valid choice.')

home_page()
