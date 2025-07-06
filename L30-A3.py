class Bird:

    def __init(self):
        print('bird is ready')

    def WhoIsThis(self):
        print('bord')
    
    def swim(self):
        print('swim faster')

class Penguin(Bird):

    def __init__(self):
        super().__init__()
        print('penguin is ready')

    def WhoIsThis(self):
        print('Penguin')

    def run(self):
        print('run faster')

peggy = Penguin()
peggy.WhoIsThis()
peggy.swim()
peggy.run()