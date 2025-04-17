string = input('please enter a string value')
string_rev = ''
for i in range(len(string)-1,-1,-1):
    string_rev = string_rev + string[i]
print(string_rev,'')