from datetime import datetime

class score:
    @staticmethod
    def load_scores(score_file):
        try:
            with open(score_file, 'r') as file:
                score = file.read()
                return int(score) if score.strip() else 0 
        except FileNotFoundError:
            print("Score file not found. Using default score of 0.")
            return 0
        except ValueError:
            print('Invalid Data in Score file')
            return 0

    @staticmethod
    def save_scores(score_file, username, win_streak):
        try:
            with open(score_file, 'a') as file:
                file.write(f"{username}, {win_streak}, {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        except IOError:
            print('Error in saving win streak')

    @staticmethod
    def view_top_scores(score_file):
        try:
            with open(score_file, 'r') as file:
                scores = []
                for line in file:
                    parts = line.strip().split(', ')
                    if len(parts) >= 3:
                        username, score, date_time = parts[:3]
                        scores.append((username, int(score), date_time))

                sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)[:10]
                print("Top Scores:")
                for idx, (username, score, date_time) in enumerate(sorted_scores, 1):
                    print(f"{idx}. {username}, High score: {score} (achieved on: {date_time})\n")
        except FileNotFoundError:
            print("Score file not found.")
