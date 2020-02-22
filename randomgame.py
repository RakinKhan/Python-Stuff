import sys
from random import randint

randomNumber = randint(1, 10)

while True:
    guess = int(input(f'Guess a number between 1 and 10: '))
    if guess > 0 and guess < 11:
        if guess == randomNumber:
            print('Congratulations! You guessed right.')
        else:
            print('Sorry! Guess again')
            continue
    else:
        print('Sorry, please guess a number between 1 and 10')
        continue
