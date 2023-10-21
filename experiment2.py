from input_recognition import InputRecognition

''' docstring '''

class MyDeriv():
    ''' docstring '''
    def __init__(self):
        self.coefficient = None
        self.variable = None
        self.exponent = None
        self.indx_coefficient = None
        self.indx_exponent = None

    def my_var(self):
        ''' docstring '''
        self.myVar = {

        }

    def assign_my_deriv(self):
        ''' docstring '''
        print("")
        print("--- 2-point Equation ---")
        print("Use the index for any monomonial you've assigned,")
        print("monomonials containing a variable will be rejected")
        print("Your polymonials:")
        print(myVar)

        self.indx_coefficient = int(input("Coefficient: "))
        self.coefficient = myVar[self.indx_coefficient][0]

        self.variable = 'x'

        self.indx_exponent = int(input("Exponent: "))
        self.exponent = myVar[self.indx_exponent][0]

    def update_my_deriv(self, coefficient, variable, exponent):
        ''' docstring '''
        self.coefficient = coefficient
        self.variable = variable
        self.exponent = exponent

    def return_parent(self):
        '''
        Returns the calculated parent, split as two rows due
        to length
        '''
        return_parent = f"{self.coefficient}{self.variable}^{self.exponent}"
        return f"parent is: {return_parent}"
    
    def print_parent(self):
        '''
        Prints the calculated parent, split as two rows due
        to length
        '''
        print_parent = f"{self.coefficient}{self.variable}^{self.exponent}"
        print(f"parent is: {print_parent}")

    def return_differenciation(self):
        '''
        Returns the calculated differenciation, split as three
        rows due to length
        '''
        return_differ_1 = f"{self.coefficient* self.exponent}"
        return_differ_2 = f"{self.variable}^{self.exponent- 1}"
        return f"differenciation is: {return_differ_1}{return_differ_2}"
    
    def print_differenciation(self):
        '''
        Prints the calculated differenciation, split as three
        rows due to length
        '''
        print_differ_1 = f"{self.coefficient* self.exponent}"
        print_differ_2 = f"{self.variable}^{self.exponent- 1}"
        print(f"differenciation is: {print_differ_1}{print_differ_2}")

run_deriv = MyDeriv()
input_recognition = InputRecognition()

input_recognition.run_input()
myVar = input_recognition.return_my_polymonial()
run_deriv.assign_my_deriv()

# End-of-file (EOF)
