import random

option = ['rock', 'paper', 'scissors']
user_score = 0
computer_score = 0

while True: 
    user_choice = input('Enter Choice by typing ROCK/PAPER/SCISSORS or Q to exit: ')

    if user_choice.lower() == 'q':
        break
    if user_choice.lower() not in option:
        continue
    
    random_number = random.randint(0, 2)
    computer_choice = option[random_number]
    
    print(f'You choose {user_choice} and Computer choose {computer_choice}')


    if user_choice == 'rock' and computer_choice == 'scissors':
        print('You win!\n')
        user_score += 1
    elif user_choice == 'scissors' and computer_choice == 'paper':
        print('You win!\n')
        user_score += 1
    elif user_choice == 'paper' and computer_choice == 'rock':
        print('You win!\n')
        user_score += 1
    elif user_choice == computer_choice:
        print('Tie, Pick again\n')
    else:
        print('you lose\n')
        computer_score += 1

print(f'The score is plyaer: {user_score} and Computer: {computer_score}\n')
print('Goodbye\n')