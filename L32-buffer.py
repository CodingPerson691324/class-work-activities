class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'i am a cat. my name is {self.name} and i am {self.age}years old')

    def make_sound(self):
        print('Meow')

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'i am a dog. my name is {self.name} and i am {self.age}years old')

    def make_sound(self):
        print('bark')

cat1 = Cat('kitty', 2.5)
dog1 = Dog('fluffy', 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()