try:
    num1,num2 = eval(int(input('enter 2 numbers seperated by a comma: ')))
    result = num1 / num2
except ZeroDivisionError as ex:
    print('exception: ',ex)
except SyntaxError as ex:
    print('exception: ',ex)
except NameError as ex:
    print('exception: ',ex)
except TypeError as ex:
    print('exception: ',ex)
except ValueError as ex:
    print('exception: ',ex)
except:
    print('WrongInput')
else:
    print('NoExceptions')