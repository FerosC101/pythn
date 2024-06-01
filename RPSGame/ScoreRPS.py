import os

class Score:
    @staticmethod
    def display_leaderboards(score_file='rps_scores.txt'):
        def read_scores(file):
            if os.path.exists(file):
                with open(file, 'r') as f:
                    scores = f.readlines()
                scores = [line.strip() for line in scores if ': ' in line]
                scores.sort(key=lambda x: int(x.split(': ')[1].split()[0]), reverse=True)
                return scores
            else:
                return []
            
        print('\nRock-Paper-Scissors Leaderboards:')
        scores = read_scores(score_file)
        for index, score in enumerate(scores, start=1):
            try:
                username, detail = score.split(': ')
                wins, date_time = detail.split(' wins on ')
                print(f'{index}. {username} - {wins} wins on {date_time}')
            except ValueError:
                print(f'{index}. Invalid score format: {score}')