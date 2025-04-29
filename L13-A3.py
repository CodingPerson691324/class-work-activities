rows = int(input('enter the number of rows: '))
if rows % 2 == 0:
    halfDiamondRow = rows // 2
else:
    halfDiamondRow = (rows // 2) + 1
space = halfDiamondRow - 1
#loop for upper part:
for i in range(1, halfDiamondRow + 1):
    for j in range(1, space + 1):
        print(end = ' ')
    space = space - 1
    num = 1
    for j in range(2 * i - 1):
        print(end = str(num))
        num = num + 1
    print('')
#loop for lower part:
space = 1
for i in range(1, halfDiamondRow):
    for j in range(1, space + 1):
        print(end = ' ')
    space = space + 1
    num = 1
    for j in range(1, 2 * (halfDiamondRow - i)):
        print(end = str(num))
        num = num + 1
    print('')