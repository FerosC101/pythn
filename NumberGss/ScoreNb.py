import os

class Score:
    @staticmethod
    def display_leaderboards(easy_score_file='easy_scores.txt', medium_score_file='medium_scores.txt', hard_score_file='hard_scores.txt'):
        def read_scores(file):
            if os.path.exists(file):
                with open(file, 'r') as f:
                    scores = f.readlines()
                scores = [line.strip() for line in scores if ': ' in line]
                scores.sort(key=lambda x: int(x.split(': ')[1].split()[0]))
                return scores
            else:
                return []

        def display_scores(scores, level_name):
            print(f'\n{level_name} Leaderboards:')
            for index, score in enumerate(scores, start=1):
                try:
                    username, detail = score.split(': ')
                    attempts, date_time = detail.split(' attempts on ')
                    print(f'{index}. {username} - {attempts} attempts on {date_time}')
                except ValueError:
                    print(f'{index}. Invalid score format: {score}')
        
        easy_scores = read_scores(easy_score_file)
        display_scores(easy_scores, 'Easy')

        medium_scores = read_scores(medium_score_file)
        display_scores(medium_scores, 'Medium')

        hard_scores = read_scores(hard_score_file)
        display_scores(hard_scores, 'Hard')
