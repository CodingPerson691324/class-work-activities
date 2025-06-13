s1 = {1,2,3}
s2 = {'a','b','c'}
s3 = list(zip(s1,s2))
print(s3)

lst1 = [10,20,30,40]
lst2 = [100,200,300,400]
for x,y in zip(lst1,lst2[::-1]):
    print(x,y)
print(list(zip(lst1,lst2[::-1])))

#dictionary comprehension

stocks = ['tesco','asda','sainsburys']
prices = [2175,1127,2750]
new_dict = {stocks:prices for stocks,prices in zip(stocks,prices)}
print(new_dict)
new_dict = {prices:stocks for prices,stocks in zip(prices,stocks)}
print(new_dict)

#list comprehension

lst = [1,2,3,4,5,6,7,8,9,0]
even_lst = [x for x in lst if x % 2 == 0]
print('list of even numbers is',even_lst)