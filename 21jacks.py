import random

cards = ["Diamonds", "Spades", "Hearts", "Clubs"]
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
    
card = random.choices(cards)
rank = random.choices(ranks)

print('Welcome to 21')
print('this is a game where you have to get cards and get as close to 21 as you can but you cant go over or you lose')
print('Ready To Play?(y/n) ')

play = input()

if play =='y':
    print('Ok. You Chose To Play.')

    print(f"The {rank} of {card}")
    print(f"The {rank} of {card}")

    if rank == 'Ace':
        print(f'you got and Ace. do you wish to ')