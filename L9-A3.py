print('select your ride')
print('1 = bike')
print('2 = car')
choice = int(input('enter your choice: '))
if choice == 1:
    print('what type of bike')
    print('1 for scootie')
    print('2 for scooter')
    choice2 = int(input('enter your choice2:'))
    if choice2 == 1:
        print('you have selected scootie')
    else:
        print('you have selected scooter')
elif choice == 2:
    print('what type of car')
    print('1 for sedan')
    print('2 = xuv')
    choice2 = int(input('enter your choice2: '))
    if choice2 == 1:
        print('you have selected sedan')
    else:
        print('you have selected xuv')
else:
    print('you have entered the wrong choice')