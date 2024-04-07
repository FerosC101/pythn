import random

number_range = input('Enter number range: ')



if number_range.isdigit():
    number_range = int(number_range)
else:
    print('Enter a number')
    quit()

random_number = random.randint(0, number_range)

guess = 0

while True:
    guess += 1
    number = input('Enter Number: ')
    if number.isdigit():
        number = int(number)
    else:
        print('Enter a number\n')
        continue

    if number == random_number:
        print('Correct!')
        break
    elif number > random_number:
        print('Go lower\n')
    else:
        print('Go Higher\n')
    
print(f'You guessed {guess} times! Congratulations')