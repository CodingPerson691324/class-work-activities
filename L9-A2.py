#take input of number of units comsumed by user
units = int(input('please enter the number of units you consumed'))

if units < 50:
    amount = units*2.60
    tax = 25
elif units <= 100:
    amount = 50*2.60+(units-50)*3.25
    tax = 35
elif units <= 200:
    amount = 50*2.60+50*3.25+(units-100)*5.26
    tax = 45
else:
    amount = 50*2.60+50*3.25+100*5.26+(units - 200)*8.45
    tax = 75
total = amount + tax
print('electricity bill = %.2f' %total)