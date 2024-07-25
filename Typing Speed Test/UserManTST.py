import json
import os

class User:
    def __init__(self, username, password, high_scores=None):
        if high_scores is None:
            high_scores = []
        self.username = username
        self.password = password
        self.high_scores = high_scores

    def add_score(self, score):
        self.high_scores.append(score)
        self.high_scores.sort(reverse=True)

class UserManager:
    def __init__(self):
        self.users = {}
        self.load_users()

    def load_users(self):
        if os.path.exists("users.json"):
            with open("users.json", "r") as file:
                user_data = json.load(file)
                for username, data in user_data.items():
                    self.users[username] = User(username, data["password"], data["high_scores"])

    def save_users(self):
        with open("users.json", "w") as file:
            user_data = {username: {
                "password": user.password,
                "high_scores": user.high_scores
            } for username, user in self.users.items()}
            json.dump(user_data, file)

    def register_user(self, username, password):
        if username in self.users:
            return False
        self.users[username] = User(username, password)
        self.save_users()
        return True

    def login_user(self, username, password):
        if username in self.users and self.users[username].password == password:
            return self.users[username]
        return None
