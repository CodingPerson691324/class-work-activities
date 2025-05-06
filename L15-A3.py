p = int(input('enter first number: '))
q = int(input('enter second number: '))
operation = int(input('enter an operation(1 for add, 2 for substract, 3 for divide, 4 for multiply): '))
def add(p,q):
    return p + q
def substract(p,q):
    return p - q
def divide(p,q):
    non_decimal = int(input('do you want to get an answer with no decimal(5 for yes, 6 for no): '))
    if non_decimal == 5:
        return p // q
    elif non_decimal == 6:
        return p / q
def multiply(p,q):
    return p * q
if operation == 1:
    print(p,'+',q,' = ',add(p,q))
if operation == 2:
    print(p,'-',q,' = ',substract(p,q))
if operation == 3:
        print(p,'/',q,' = ',divide(p,q))
if operation == 4:
    print(p,'*',q,' = ',multiply(p,q))