for r in range(1,6):

    for c in range(4,r-1,-1):
        print(' ',end='')

    for c in range(0,r):
        print('*',end='')

    print()
    