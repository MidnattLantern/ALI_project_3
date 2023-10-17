''' docstring '''

class myLinear2pEquation():
    ''' docstring '''
    def __init__(self):
        self.y1 = 0
        self.y2 = 0
        self.x1 = 0
        self.x2 = 0

    def update_2p(self, y1, y2, x1, x2):
        ''' docstring '''
        self.y1 = y1
        self.y2 = y2
        self.x1 = x1
        self.x2 = x2

    def update_input(self):
        ''' docstring '''
        y1 = int(input("y1: "))
        y2 = int(input("y2: "))
        x1 = int(input("x1: "))
        x2 = int(input("x2: "))
        self.update_2p(y1, y2, x1, x2)

    def print_2p(self):
        ''' docstring '''
        print(self.y1)
        print(self.y2)
        print(self.x1)
        print(self.x2)

my_int = myLinear2pEquation()
my_int.print_2p()
my_int.update_input()
my_int.print_2p()

# End-of-file (EOF)
