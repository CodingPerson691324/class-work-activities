print('enter marks obtained in 3 subjects')
mark1 = int(input())
mark2 = int(input())
mark3 = int(input())
total = mark1+mark2+mark3
average = total/3
if average>=91:
    print('your grade is A1')
elif average>=81:
    print('your grade is A2')
elif average>=71:
    print('your grade is B1')
elif average>=61:
    print('your grade is B2')
elif average>=51:
    print('your grade is C1')
elif average>=41:
    print('your grade is C2')
elif average>=31:
    print('your grade is D1')
else:
    print('you are failed')