import random
while True:
    user_action = input('enter a choice between rack, paper or scissors: ')
    possible_actions = ['rock' ,'paper', 'scissors' ]
    computer_action = random.choice(possible_actions)
    print('you chose',user_action,'and computer chose',computer_action)
    if user_action == computer_action:
        print('both players selected the',user_action,'its a tie')
    elif user_action == 'rock':
        if computer_action == 'scissors':
            print('rock smashes scissors (You win)')
        else:
            print('paper covers rock (you lose)')
    elif user_action == 'paper':
        if computer_action == 'rock':
            print('paper covers rock (you win)')
        else:
            print('scissors cut paper (you lose)')
    elif user_action == 'scissors':
        if computer_action == 'paper':
            print('scissors cuts paper (you win)')
        else:
            print('rock smashes scissors (you lose)')
    play_again = input('do u want to play again (y/n): ')
    if play_again == 'n':
        print('goodbye!')
        break