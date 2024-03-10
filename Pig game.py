import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    player = input('Enter Number of Players(1-4): ')
    if player.isdigit():
        player = int(player)
        if 2 <= player <= 4:
            break
        else:
            print('Number must be 2-4')
    else:
        print('Invalid PLayer number!')

print(player)

total_score = 50
player_score = [0 for i in range(player)]

while max(player_score) < total_score:
    for player_i in range(player):
        print(f'\nPlayer {player_i + 1} turn has just started!')
        print(f'Your total score is: {player_score[player_i]}\n')
        current_score = 0

        while True:
            should_roll = input('Would you like to roll (y)? ')
            if should_roll.lower() != 'y':
                break
            
            value = roll()
            if value == 1:
                print('You rolled a 1! RESET SCORE!')
                current_score = 0
                break
            else:
                current_score += value
                print(f'You rolled a: {value}')
            
            print(f'Your score is:{current_score}')

        player_score[player_i] == current_score
        print(f'Your total score is: {player_score[player_i]}')

max_score = max(player_score)
winning_idx = player_score.index(max_score)
print(f'Player number {winning_idx + 1} is the winner with a score of of: {max_score}')