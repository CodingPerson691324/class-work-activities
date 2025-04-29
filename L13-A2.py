print('half pyramid pattern of numbers: ')
n = int(input('enter the number of rows: '))
count = 1
for i in range(n):
    for j in range(i + 1):
        print(count,end = ' ')
        count = count + 1
    print('')