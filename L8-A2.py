print('enter a number(numerator)')
numn = int(input())
print('enter a number(denominator)')
numb = int(input())
if numn%numb == 0:
    print(numn,'is divisible by',numb)
else:
    print(numn,'is not divisible by',numb)