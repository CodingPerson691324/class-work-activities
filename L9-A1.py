#take input for student whether can attend exam or not
medical_cause = input('Did you have a medical cause? (y for yes, n for no): ')
atten = int(input('enter the attendace of the student'))
#checking the user input and then predicting the output accordingly
if medical_cause == 'y':
    print('you are allowed')
else:
    if atten >= 75:
        print('you are allowed')
    else:
        print('you are not allowed')