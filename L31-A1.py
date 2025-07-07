class myClass:

    __privateVar = 27

    def __priMeth(self):
        print('im inside the class myClass')

    def hello(self):
        print('private variable value:', myClass.__privateVar)

foo = myClass()
foo.hello()
foo.__priMeth