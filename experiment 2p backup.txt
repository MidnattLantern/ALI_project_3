from input_recognition import InputRecognition

class My2pEquation():
    ''' docstring '''
    def __init__(self):
        self.x1 = None
        self.x2 = None
        self.y1 = None
        self.y2 = None

    def my_var(self):
        ''' docstring '''
        self.myVar = {

        }

    def assign_points(self):
        ''' docstring '''
        print("")
        print("--- 2-point Equation ---")
        print("Use the index for any monomonial you've assigned,")
        print("monomonials containing a variable will be rejected")
        print("Your polymonials:")
        print(myVar)
        self.x1 = int(input("Point x1: "))
        self.x2 = int(input("Point x2: "))
        self.y1 = int(input("Point y1: "))
        self.y2 = int(input("Point y2: "))
        print('------')

    def reveal_2p_equation(self, x1, x2, y1, y2):
        ''' checking that all are assigned a value '''
        if all(var is not None for var in [x1, x2, y1, y2]):
            try:
                k = ( y2 - y1) / ( x2 - x1)
                print("k value for 2p equation is: "+ str(k))
            except ZeroDivisionError:
                print("k value for 2p equation is: 0")
        else:
            print("error: either of the point(s) are unassigned")

run_2p_equation = My2pEquation()
input_recognition = InputRecognition()
input_recognition.run_input()
myVar = input_recognition.return_my_polymonial()
run_2p_equation.assign_points()
print(run_2p_equation.x1)