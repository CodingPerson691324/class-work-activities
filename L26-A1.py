num1 = [1,2,3]
num2 = [4,5,6]
result = map(lambda x,y:x+y,num1,num2)
print('the addition of 2 list is',list(result))

nums = [0,1,2,3,4,5]
def square(n):
    return n**2
sq = list(map(square,nums))
print('the square of numbers in a list is',sq)