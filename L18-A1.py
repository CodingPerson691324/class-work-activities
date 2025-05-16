num = int(input('please enter a number: '))
try:
    div = 1 / num
    print(div)
except:
    print('the division is not possible')
finally:
    print('this block will run')