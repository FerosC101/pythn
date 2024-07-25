import json
import time
import os

class MainMenu:
    def __init__(self, user_manager, dorm_system):
        self.user_manager = user_manager
        self.dorm_system = dorm_system
        self.current_user = None

    def greetings(self):
        text_appear_time('\nWelcome to MyDormie\n', 0.04)
        text_appear_time('Having a hard time finding your dorm or apartment? well you\'re in luck because MyDormie will help you out!\n\n', 0.04)

        input('Press any key to continue :>')
        self.display_menu()

    def display_menu(self):
        print('Welcome to MyDormie')
        while True:
            print('1. Register')
            print('2. Login')
            print('3. Exit')
            choice = int(input('Enter Choice: '))
            if choice == 1:
                self.register()
            elif choice == 2:
                self.login()
            elif choice == 3:
                break

    def register(self):
        username = input('Enter Username: ')
        password = input('Enter Password: ')
        if self.user_manager.acc_register(username, password):
            print('Registration Successful!\n')
        else:
            print('Username already exists.\n')

    def login(self):
        username = input('Enter Username: ')
        password = input('Enter Password: ')
        if self.user_manager.acc_login(username, password):
            print('Login Successful!\n')
            self.current_user = username
            self.user_menu()
        else:
            print('Invalid username or password\n')

    def user_menu(self):
        while True:
            text_appear_time(f'\nWelcome {self.current_user}\n', 0.04)
            print('1. Show Available Dorms')
            print('2. Show Map of GCH')
            print('3. Dorm Information')
            print('4. Reserve a Room')
            print('5. Submit Maintenance Request')
            print('6. Add Dorm Block')
            print('7. Add House to Block')
            print('8. Logout')
            choice = int(input('Enter Choice: '))
            if choice == 1:
                self.dorm_system.show_available_dorms()
            elif choice == 2:
                self.dorm_system.show_map()
            elif choice == 3:
                self.dorm_system.dorm_info()
            elif choice == 4:
                self.dorm_system.reserve_room()
            elif choice == 5:
                self.dorm_system.submit_maintenance_request()
            elif choice == 6:
                self.dorm_system.add_dorm_block()
            elif choice == 7:
                self.dorm_system.add_house_to_block()
            elif choice == 8:
                self.display_menu()
                break

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def to_database(self):
        return {
            'username': self.username,
            'password': self.password
        }
    
class UserManager:
    def __init__(self, user_file='users.json'):
        self.user_file = user_file
        self.users = self.load_users()

    def load_users(self):
        if os.path.exists(self.user_file):
            with open(self.user_file, 'r') as file:
                return json.load(file)
        return {}
    
    def save_users(self):
        with open(self.user_file, 'w') as file:
            json.dump(self.users, file)

    def acc_register(self, username, password):
        if username in self.users:
            return False
        self.users[username] = User(username, password).to_database()
        self.save_users()
        return True
    
    def acc_login(self, username, password):
        if username in self.users and self.users[username]['password'] == password:
            return True
        return False
    
class DormSystem:
    def __init__(self):
        self.dorms = self.initialize_dorms()
        self.maintenance_requests = []

    def initialize_dorms(self):
        dorms = {
            'Block A': {
                'House 1': {'rent_price': 500, 'current_tenant': None},
                'House 2': {'rent_price': 550, 'current_tenant': None},
                'House 3': {'rent_price': 600, 'current_tenant': None},
                'House 4': {'rent_price': 550, 'current_tenant': None}
            },
            'Block B': {
                'House 1': {'rent_price': 450, 'current_tenant': None},
                'House 2': {'rent_price': 500, 'current_tenant': None},
                'House 3': {'rent_price': 550, 'current_tenant': None},
                'House 4': {'rent_price': 600, 'current_tenant': None}
            },
            'Block C': {
                'House 1': {'rent_price': 600, 'current_tenant': None},
                'House 2': {'rent_price': 650, 'current_tenant': None},
                'House 3': {'rent_price': 700, 'current_tenant': None},
                'House 4': {'rent_price': 750, 'current_tenant': None}
            }
        }
        return dorms

    def show_available_dorms(self):
        print("\nAvailable Dorms:")
        for block, houses in self.dorms.items():
            print(f"{block}:")
            for house, details in houses.items():
                if details['current_tenant'] is None:
                    print(f"  {house}: Rent Price: ${details['rent_price']} | Available")
                else:
                    print(f"  {house}: Rent Price: ${details['rent_price']} | Tenant: {details['current_tenant']}")
        print()

    def show_map(self):
        map_lines = [
            " Golden Country Homes, Alangilan, Batangas City, Batangas, Philippines",
            "",
            "  +------------------------------------------------------------------+",
            "  |                       Entrance/Exit                              |",
            "  |                        |-----------------------|                 |",
            "  |                        |       Main Road       |                 |",
            "  |                        |-----------------------|                 |",
            "  |                                 |                                |",
        ]

        for block, houses in self.dorms.items():
            map_lines.append(f"  |    +---------+    +---------+    +---------+    +---------+   |")
            map_lines.append(f"  |    | {block:<7} |    | {block:<7} |    | {block:<7} |    | {block:<7} |   |")
            map_lines.append(f"  |    |---------|    |---------|    |---------|    |---------|   |")

            for house, details in houses.items():
                tenant_info = details['current_tenant'] if details['current_tenant'] else 'Available'
                map_lines.append(f"  |    | {house:<7} |    | {house:<7} |    | {house:<7} |    | {house:<7} |   |")
                map_lines.append(f"  |    | Rent: ${details['rent_price']:<30} | Tenant: {tenant_info:<15} |")

            map_lines.append(f"  |    +---------+    +---------+    +---------+    +---------+   |")

        map_lines += [
            "  |                                 |                                |",
            "  |                                                                  |",
            "  +-----------------------------------------------------------------+",
            ""
        ]

        for line in map_lines:
            print(line)

    def dorm_info(self, block_name, house_name):
        if block_name in self.dorms and house_name in self.dorms[block_name]:
            details = self.dorms[block_name][house_name]
            if details['current_tenant']:
                print(f"\nInformation for {block_name} - {house_name}: Rent Price: ${details['rent_price']}, Current Tenant: {details['current_tenant']}\n")
            else:
                print(f"\nInformation for {block_name} - {house_name}: Rent Price: ${details['rent_price']}, Available\n")
        else:
            print('\nDorm not found.\n')

    def reserve_room(self, block_name, house_name, tenant_name):
        if block_name in self.dorms and house_name in self.dorms[block_name]:
            if self.dorms[block_name][house_name]['current_tenant'] is None:
                self.dorms[block_name][house_name]['current_tenant'] = tenant_name
                print(f'\nRoom reserved successfully in {block_name} - {house_name} for {tenant_name}.\n')
            else:
                print(f'\n{block_name} - {house_name} is already occupied.\n')
        else:
            print('\nDorm not found.\n')

    def submit_maintenance_request(self):
        pass

    def add_dorm_block(self):
        pass

    def add_house_to_block(self):
        pass

    

def text_appear_time(message, delay):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(delay)

if __name__ == '__main__':
    user_manager = UserManager()
    dorm_system = DormSystem()
    main_menu = MainMenu(user_manager, dorm_system)
    main_menu.greetings()
