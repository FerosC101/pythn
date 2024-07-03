import os

class Score:
    @staticmethod
    def display_leaderboards(score_file='hangman_scores.txt'):
        def read_scores(file):
            if os.path.exists(file):
                with open(file, 'r') as f:
                    scores = f.readlines()
                scores = [line.strip() for line in scores if ': ' in line]
                scores.sort(key=lambda x: float(x.split(': ')[1].split()[0]))
                return scores
            else:
                return []
            
        print('\nHangman Leaderboards: ')
        scores = read_scores(score_file)
        for index, score in enumerate(scores, start=1):
            try:
                username, detail = score.split(': ')
                time_taken, date_time = detail.split('seconds on ')
                print(f'{index}. {username} - {time_taken} seconds on {date_time}')
            except ValueError:
                print(f'{index}. Invalid score format: {score}')