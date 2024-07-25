class UserManager:
    @staticmethod
    def load_users():
        try:
            with open("User_Data.txt", "r") as file:
                lines = file.readlines()

            users = {}
            for line in lines:
                data = line.strip().split(",")  
                if len(data) == 3:  
                    username, password, score = data
                    users[username] = (password, int(score))  
                else:
                    pass

            return users
        except FileNotFoundError:
            print("Error: Users file not found.")
            return {}

        
    @staticmethod
    def save_users(users):
        with open('User_Data.txt', 'w') as file:
            for username, (password, score) in users.items():
                file.write(f'{username},{password},{score}\n')

    @staticmethod
    def validate_username(username, users):
        if username in users:
            print("Username already exists. Please choose a different one.")
            return False
        return True
    
    @staticmethod
    def validate_password(password):
        while True:
            if len(password) < 8:
                print('Password must be at least 8 characters long')
                password = input('Enter Password: ')
                continue
            return password
            
