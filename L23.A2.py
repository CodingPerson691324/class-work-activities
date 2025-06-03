dict_ = {'codingal':2,'is':2,'best':2,'for':2,'coding':1}
count = 0
k = 2
for key in dict_:
    if dict_[key] == k:
        count = count + 1
print('frequency of k is',count)