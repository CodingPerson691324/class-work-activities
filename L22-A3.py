weather = (1,0,0,0,1,1,0)
sunny = 0
rainy = 0
for i in range(len(weather)):
    if weather[i] == 1:
        rainy += 1
    else:
        sunny += 1
if sunny > rainy:
    print('the forecast is sunny')
else:
    print('the weather is rainy')