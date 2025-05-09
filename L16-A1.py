num = int(input('enter a positive interger: '))
def prime(num):
    if num <= 1:
        return 0
    for i in range(2,int(num ** 0.5)+ 1):
        if num % i == 0:
            return 0
    return 1
if prime(num) == 0:
    print(num,'is not a prime number')
else:
    print(num,'is a prime number')