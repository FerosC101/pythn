import os
import json

class User:
    def __init__(self, username, password, wins=0,losses=0):
        self.username = username
        self.password = password
        self.wins = wins
        self.losses = losses

    def to_dict(self):
        return {
            'username' : self.username,
            'password' : self.password,
            'wins' : self.wins,
            'losses' : self.losses
        }
    
class UserManager:
    def __init__(self, user_file = 'users.json'):
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

    def register(self, username, password):
        if username in self.users:
            return False
        self.users[username] = User(username, password).to_dict()
        self.save_users()
        return True
    
    def login(self, username, password):
        if username in self.users and self.users[username]['password'] == password:
            return True
        return False
    
    def validate_info(self, username, password):
        if username < 4:
            print('Username must be at least 4 characters long.')
            return False
        if password < 6:
            print('Password must be at least 6 characters long.')
            return False
        return True
    
    def update_record(self, username, result):
        if result == 'win':
            self.users[username]['wins'] += 1
        elif result == 'loss':
            self.users[username]['losses'] += 1
        self.save_users()

    def get_user_record(self, username):
        if username in self.users:
            return self.users[username]['wins'], self.users[username]['losses']
        return None