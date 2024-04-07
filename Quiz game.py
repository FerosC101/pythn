print('WELCOME TO QUIZ GAME!')

choice = input('Do you wish to play?(press y): ')

if choice.lower() != 'y':
    print('maybe next time')
    quit()

print('Welcome Player!\n')

Score = 0

answer = input('What does CPU stands for? ')
if answer.lower() == 'central processing unit':
    print('Correct')
    Score += 1
else:
    print('IncorrectS\n')

answer = input('What is the power house of the cell? ')
if answer.lower() == 'mitochondria':
    print('Correct')
    Score += 1
else:
    print('Incorrect\n')

answer = input('What does RAM stands for? ')
if answer.lower() == 'read all memory':
    print('Correct')
    Score += 1
else:
    print('Incorrect\n')

answer = input('What is the atomic number of hydrogen? ')
if answer.lower() == '1':
    print('Correct')
    Score += 1
else:
    print('Incorrect\n')

answer = input('What is the largest ocean? ')
if answer.lower() == 'pacific ocean':
    print('Correct')
    Score += 1
else:
    print('Incorrect\n')

print(f'great job you got {Score} out of 5!')