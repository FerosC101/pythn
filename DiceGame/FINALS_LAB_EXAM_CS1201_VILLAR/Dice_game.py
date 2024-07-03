import random
from datetime import datetime
from Score import score

class dicegame:
    def __init__(self, score_file, match_history_file):
        self.score_file = score_file
        self.match_history_file = match_history_file
    
    def save_match_history(self, username, match_result, score, date_time):
        try:
            with open(self.match_history_file, 'a') as file:
                file.write(f"{username}, {match_result}, {score}, {date_time}\n")
        except IOError:
            print('Error in saving match history')

    def play_game(self, username):
        while True:
            current_streak = 0
            best_streak = score.load_scores(self.score_file)  

            while True:
                user_score = 0
                computer_score = 0

                while True:
                    user_roll = random.randint(1, 6)
                    computer_roll = random.randint(1, 6)
                    print(f'{username} rolled: {user_roll} and Computer rolled: {computer_roll}')

                    if user_roll > computer_roll:
                        print('Winner: User\n')
                        user_score += 1
                        current_streak += 1
                        if current_streak > best_streak:
                            best_streak = current_streak 
                    elif user_roll == computer_roll:
                        print('It\'s a Tie\n')
                    else:
                        print('Winner: Computer\n')
                        current_streak = 0 
                        break

                    print(f'Total Score, User: {user_score}, Computer: {computer_score}')

                print("----- New Round -----") 

                print(f'Best Win streak: {best_streak}')
                print('Game Over')
                print(f'Final Score, User: {user_score}, Computer: {computer_score}')

                score.save_scores(self.score_file, username, best_streak)

                choice_again = input('Do you want to play again? (Y/N): ')
                if choice_again.strip().upper() != 'Y':
                    print(f'Your best win streak is {best_streak}!')
                    return False
                else:
                    print('\n----- Next Round -----\n')


    def view_top_scores(self):
        score.view_top_scores(self.score_file)