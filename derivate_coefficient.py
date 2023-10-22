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
        print("--- Derivate ---")
        print("Use the index for any monomonial you've assigned,")
        print("monomonials containing a variable will be rejected")
        print("Your polymonials:")
        print(myVar)

        self.indx_coefficient = int(input("Coefficient: "))
        try:
            self.coefficient = myVar[self.indx_coefficient][0]
            print("Set coefficient to: "+ str(self.coefficient))
        except KeyError:
            print("there is no monomonial for this index")

        self.variable = 'x'

        self.indx_exponent = int(input("Exponent: "))
        try:
            self.exponent = myVar[self.indx_exponent][0]
            print("Set exponent to: "+ str(self.exponent))
        except KeyError:
            print("There is no monomonial for this index")

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
        print('    ------')
        print('')
        print(f"    parent is: {print_parent}")
        print('')


    def return_differenciation(self):
        '''
        Returns the calculated differenciation, split as three
        rows due to length
        '''
        try:
            differ_1 = int(self.coefficient)* int(self.exponent)
            differ_2 = int(self.exponent)- 1
            return_differ_1 = f"{differ_1}"
            return_differ_2 = f"{self.variable}^{differ_2}"
            return f"differenciation is: {return_differ_1}{return_differ_2}"
        except (TypeError, ValueError):
            pass
    
    def print_differenciation(self):
        '''
        Prints the calculated differenciation, split as three
        rows due to length
        '''
        if all(var is not None for var in [self.coefficient, self.exponent]):
            try:
                differ_1 = int(self.coefficient)* int(self.exponent)
                differ_2 = int(self.exponent)- 1
                print_differ_1 = f"{differ_1}"
                print_differ_2 = f"{self.variable}^{differ_2}"
                print('    ------')
                print('')
                print(f"    differenciation is: {print_differ_1}{print_differ_2}")
                print('')
            except (ValueError):
                print("    ------")
                print("")
                print("    Monomonials containing variables and/ or exponents are not supported.")
                print("")
        else:
            print("Error: either was assigned an index for monomonial that does not exist")


    def run(self):
        ''' bundle all strings to execute all '''
        run_deriv.assign_my_deriv()
        run_deriv.return_parent()
        run_deriv.print_parent()
        run_deriv.return_differenciation()
        run_deriv.print_differenciation()

        #test
        self.coefficient = None
        self.variable = None
        self.exponent = None
        self.indx_coefficient = None
        self.indx_exponent = None


run_deriv = MyDeriv()
input_recognition = InputRecognition()

input_recognition.run_input()
myVar = input_recognition.return_my_polymonial()
run_deriv.run()

# End-of-file (EOF)
