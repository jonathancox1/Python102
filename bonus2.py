import random
#number getting game 
#give user 5 chances
#attempt = 5

#accept user input
guess = int(input('Guess  a number 1-10 '))

#create random number
random_number = random.randint(0, 9)

for i in range(5,0,-1):
    if guess == random_number:
        print('Correct Guess!')
        break
    else:
        print('Incorrect Guess')
        print(f'{i} attempts left')
        guess = int(input('Guess  a number 1-10 '))





#determine if guess == random number
# print(f'Guesses left: {attempt}')
# if guess == random_number:
#     print(f'You\'ve guessed the random number {random_number}')
# elif guess != random_number:
#     print('4 attempts left')
#     guess = int(input('Guess  a number 1-10'))
#     if guess == random_number:
#         print(f'You\'ve guessed the random number {random_number}')
# elif guess != random_number:
#     print('3 attempts left')
#     guess = int(input('Guess  a number 1-10'))
#     if guess == random_number:
#         print(f'You\'ve guessed the random number {random_number}')
# elif guess != random_number:
#     print('2 attempts left')
#     guess = int(input('Guess  a number 1-10'))
#     if guess == random_number:
#         print(f'You\'ve guessed the random number {random_number}')
# elif guess != random_number:
#     print('2 attempts left')
#     guess = int(input('Guess  a number 1-10'))
#     if guess == random_number:
#         print(f'You\'ve guessed the random number {random_number}')
# elif guess != random_number:
#     print('1 attempts left')
#     guess = int(input('Guess  a number 1-10'))
#     if guess == random_number:
#         print(f'You\'ve guessed the random number {random_number}')
# else:
#     print('0 attpemts left')
#     print('Game Over')

