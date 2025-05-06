def weather_condition():
    x = 2
    print('the value of x inside function is:',x)
    print('the weather is pleasant in',spring)
    print('the weather is the same in',autumn)
    return x

spring = 'autumn'
autumn = spring
x = weather_condition()
print('the value of x outside function is:',x)