lst = [132,4,69,48]
count = 0
for i in lst:
    count = count + i
print('the sum of numbers of the list is',count)
print('the average of the numbers in the list is',count / len(lst))

lst.sort()
print('the sorted list looks like',lst)
print('the smallest element of the list is',lst[0])
print('the largest element of the list is',lst[-1])