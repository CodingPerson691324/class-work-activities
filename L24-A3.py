import array as arr
lst = [1,3,5,3,1,2,5,1,6,9,6,3,1,1,1,1,1,1,1,1,1,1,1,1,1]
array_num = arr.array('i',lst)
print(array_num)

print('number of occurences of 1 is',array_num.count(1))

array_num.reverse()
print(array_num)

arr_num1 = arr.array('d',[1.1,2.2,3.4,5.7])
print(arr_num1)
array_num.insert(1,4)
print(array_num)