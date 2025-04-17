#input an integer value
n = int(input('enter a number whos sum you want to find: '))
sum = 0
#iterates for n number of times 
for i in range(1, n + 1):
    sum = sum + i
    print(i,' ',sum)