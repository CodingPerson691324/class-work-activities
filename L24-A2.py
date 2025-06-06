set1 = {'green',1,'blue'}
set2 = {'blue','yellow',1}
print('original set elements are')
print(set1)
print(set2)
print('intersection of the two sets are')
intersection_set = set1.intersection(set2)
print(intersection_set)

print('intersection of the two sets are')
union_set = set1.union(set2)
print(union_set)

print('difference of the two sets are')
difference_set = set1.difference(set2)
print(difference_set)

print('difference of the two sets are')
difference_set = set2.difference(set1)
print(difference_set)

print('symmetric_difference of the two sets are')
symmetric_difference = set1.symmetric_difference(set2)
print(symmetric_difference)