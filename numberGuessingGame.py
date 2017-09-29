#Gary Li
#9/29/17
#numberGuessingGame.py

from random import randint

number = randint(1,100)

numTries=1
while True:
    guess = int(input('Guess a number between 1 and 100: '))
    if guess < number:
        print('too low')
    elif guess>number:
        print('too high')
    else:
        break
    numTries = numTries+1

print('You got it in', numTries, 'tries!')
