n = int(input('enter a number to check if it is an armstrong number: '))
sum = 0
temp = n
while temp > 0:
    rem = temp % 10
    temp = temp // 10
    sum = sum + rem**3
if sum == n:
    print(n,'is an armstrong number')
else:
    print(n,'is not an armstrong number')