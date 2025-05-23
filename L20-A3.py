def hotel_cost(nights):
    return 140 * nights
def plane_ride_cost(city):
    if city == 'charlotte':
        return 183
    elif city == 'tempa':
        return 220
    elif city == 'pittsburgh':
        return 222
    elif city == 'los angeles':
        return 475
def rental_car_cost(days):
    if days >= 7:
        return 40*days-50
    elif days >= 3:
        return 40*days-20
    else:
        return 40*days
def trip_cost(city,days,spending_money):
    return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money
print('total cost of your trip is',trip_cost('los angeles',7,300))