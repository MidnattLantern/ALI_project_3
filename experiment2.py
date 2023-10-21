from input_recognition import InputRecognition

class My2pEquation():
    ''' docstring '''
    def __init__(self):
        self.x1 = None
        self.x2 = None
        self.y1 = None
        self.y2 = None
        self.indx_x1 = None
        self.indx_x2 = None
        self.indx_y1 = None
        self.indx_y2 = None

    def my_var(self):
        ''' docstring '''
        self.myVar = {

        }

    def assign_2p_indx(self):
        ''' docstring '''
        print("")
        print("--- 2-point Equation ---")
        print("Use the index for any monomonial you've assigned,")
        print("monomonials containing a variable will be rejected")
        print("Your polymonials:")
        print(myVar)
        self.indx_x1 = int(input("Point x1: "))
        self.x1 = myVar[self.indx_x1][0]
        print("set x1 to: "+ str(self.x1))

        self.indx_x2 = int(input("Point x2: "))
        self.x2 = myVar[self.indx_x2][0]
        print("set x2 to: "+ str(self.x2))

        self.indx_y1 = int(input("Point y1: "))
        self.y1 = myVar[self.indx_y1][0]
        print("set y1 to: "+ str(self.y1))

        self.indx_y2 = int(input("Point y2: "))
        self.y2 = myVar[self.indx_y2][0]
        print("set y2 to: "+ str(self.y2))

        print('------')

    def reveal_2p_equation(self, x1, x2, y1, y2):
        ''' checking that all are assigned a value '''
        if all(var is not None for var in [x1, x2, y1, y2]):

            print('')
            print('    '+ str(y2)+ ' - '+ (str(y1)))
            print('k = ------------ = ')
            print('    '+ str(x2)+ ' - '+ (str(x1)))
            print('')

            try:
                k = (int(y2) - int(y1)) / ( int(x2) - int(x1))
                print("k value for 2p equation is: "+ str(k))
            except ZeroDivisionError:
                print("k value for 2p equation is: 0")
        else:
            print("error: either of the point(s) are unassigned")
    
    def run(self):
        ''' only func to use '''
        self.assign_2p_indx()
        self.reveal_2p_equation(self.x1, self.x2, self.y1, self.y2)

run_2p_equation = My2pEquation()
input_recognition = InputRecognition()
input_recognition.run_input()
myVar = input_recognition.return_my_polymonial()
run_2p_equation.run()