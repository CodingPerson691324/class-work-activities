class Vehicles:

    def __init__(self, vehicleType):
        print('Vehicles is a', vehicleType)

class Car(Vehicles):

    def __init__(self):
        Vehicles.__init__(self, 'Car')

print(issubclass(Car, Vehicles))
print(issubclass(Car, list))
print(issubclass(Car, Car))
print(issubclass(Car, (list, Vehicles)))