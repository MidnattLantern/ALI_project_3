from input_recognition import InputRecognition


class MyDeriv():
    '''
    Setup for mathematical elements,
    used to calculate derivate.
     Updated from "update_my_deriv"
    '''
    def __init__(self):
        self.coefficient = None
        self.variable = None
        self.exponent = None
        self.indx_coefficient = None
        self.indx_exponent = None

    def my_var(self):
        '''
        myVar aka "my_polynomial"
        Imported from input_recognition.py
        Future version should import from run.py
        '''
        self.myVar = {

        }

    def assign_my_deriv(self):

        '''
        UI
        '''
        print("")
        print("--- Derivate ---")
        print("Use the index for any monomonial you've assigned,")
        print("monomonials containing a variable will be rejected")
        print("Your polymonials:")
        print(myVar)

        try:
            self.indx_coefficient = int(input("Coefficient: \n"))
            self.coefficient = myVar[self.indx_coefficient][0]
            print("Set coefficient to: " + str(self.coefficient))
        except (ValueError, KeyError):
            print("there is no monomonial for this index")

        self.variable = 'x'

        try:
            self.indx_exponent = int(input("Exponent: \n"))
            self.exponent = myVar[self.indx_exponent][0]
            print("Set exponent to: " + str(self.exponent))
        except (ValueError, KeyError):
            print("There is no monomonial for this index")

    def update_my_deriv(self, coefficient, variable, exponent):
        '''
        From the setup earlier, these replace "None" with user's
        input
        '''
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
            differ_1 = int(self.coefficient) * int(self.exponent)
            differ_2 = int(self.exponent) - 1
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
                differ_1 = int(self.coefficient) * int(self.exponent)
                differ_2 = int(self.exponent) - 1
                print_differ_1 = f"{differ_1}"
                print_differ_2 = f"{self.variable}^{differ_2}"
                print('------')
                print('')
                print(f"differenciation is: {print_differ_1}{print_differ_2}")
                print('')
            except (ValueError):
                print("------")
                print("")
                print("Monomonials containing variables and/")
                print("or exponents are not supported.")
                print("")
        else:
            print("")
            print("Error: Either was assigned an index for")
            print("a monomonial that does not exist")

    def run(self):
        ''' bundle all strings to execute all '''
        run_deriv.assign_my_deriv()
        run_deriv.return_parent()
        run_deriv.print_parent()
        run_deriv.return_differenciation()
        run_deriv.print_differenciation()
        self.coefficient = None
        self.variable = None
        self.exponent = None
        self.indx_coefficient = None
        self.indx_exponent = None


run_deriv = MyDeriv()
input_recognition = InputRecognition()
myVar = input_recognition.return_my_polymonial()

if __name__ == '__main__':
    input_recognition.run_input()
    run_deriv.run()

# End-of-file (EOF)
