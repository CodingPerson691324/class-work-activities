while True:
    num = int(input('enter a positive interger: '))
    if num == 0:
        break
    def fact(num):
        temp = num
        prod = 1
        for i in range(num):
            prod = prod * temp
            temp = temp - 1
        return prod
    print(num,'! =',fact(num))
    