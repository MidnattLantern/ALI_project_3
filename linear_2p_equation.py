''' docstring '''

class myLinear2pEquation():
    ''' docstring '''
    def __init__(self):
        self.y1 = 0
        self.y2 = 0
        self.x1 = 0
        self.x2 = 0

    def update_2p(self, y1, y2, x1, x2):
        '''
        inappropriate to use for calling, use
        update_input() instead
        '''
        self.y1 = y1
        self.y2 = y2
        self.x1 = x1
        self.x2 = x2

    def update_my_input(self):
        '''
        appropriate to use for calling
        '''
        y1 = int(input("y1: "))
        y2 = int(input("y2: "))
        x1 = int(input("x1: "))
        x2 = int(input("x2: "))
        self.update_2p(y1, y2, x1, x2)

    def calculate_2p(self):
        ''' docstring '''
        k = (self.y2 - self.y1) / (self.x2 - self.x1)
        print(k)

    def print_2p(self):
        ''' docstring '''
        print(self.y1)
        print(self.y2)
        print(self.x1)
        print(self.x2)

my_2p = myLinear2pEquation()
my_2p.update_my_input()
my_2p.calculate_2p()
my_2p.print_2p()

# End-of-file (EOF)
