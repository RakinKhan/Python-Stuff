from random import randint
import sys

randomNumber = randint(int(sys.argv[1]), int(sys.argv[2]))
print(randomNumber)

while True:

    guess = input('Guess a number between 1 and 10: ')
    try:
        if int(guess) > 0 and int(guess) < 11:
            if int(guess) == randomNumber:
                print('Congratulations! You guessed right.')
                break
            else:
                print('Sorry! Guess again')
                continue
        else:
            print('Sorry, please guess a number between 1 and 10')
            continue
    except ValueError:
        print('Use the number buttons')
        continue
