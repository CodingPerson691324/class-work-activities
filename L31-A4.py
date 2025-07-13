class Student:
    def __init__(self, name, grade):
        self.__name = name
        self.__grade = grade

    def get_grade(self):
        return self.__grade
    
    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print('invalid grade')

s = Student('Alice', 85)
print(s.get_grade())
s.set_grade(95)
print(s.get_grade())