import os

class Score:
    @staticmethod
    def display_leaderboards(score_file='ws_scores.txt'):
        def read_scores(file):
            if os.path.exists(file):
                with open(file, 'r') as f:
                    scores = f.readlines()
                scores = [line.strip() for line in scores]
                scores.sort(key=lambda x: (-int(x.split(' correct guesses in ')[0].split(': ')[1]), float(x.split(' correct guesses in ')[1].split(' seconds on ')[0])))
                return scores
            else:
                return []
        
        print('Word Scramble Leaderboards:')
        scores = read_scores(score_file)
        for index, score in enumerate(scores, start=1):
            username, detail = score.split(': ')
            guesses, rest = detail.split(' correct guesses in ')
            time, date_time = rest.split(' seconds on ')
            print(f'{index}. {username} - {guesses} correct guesses in {time} seconds on {date_time}')