import random
number = int(random.randint(0,10))
print('i will generate a number form 0 to 10 and u have to guess the number one digit at a time')
while True:
    guess = int(input('enter a number between 0 - 10: '))
    if number == guess:
        print('you won the game!')
        break
    else:
        print('your guess is not quite right try again: ')