r = (1,2,3,3,2,1)
def palindrome(r):
    e = len(r) - 1
    s = 0
    while s < e:
        if r[s] != r[e]:
            return False
        s =s + 1
        e = e - 1
    return True
if palindrome(r) == True:
    print('your number is a palindrome')
else:
    print('your number is not a palindrome')
