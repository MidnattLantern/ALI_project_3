''' docstring '''

class MyDeriv():
    ''' docstring '''
    def __init__(self):
        self.coefficient = None
        self.variable = None
        self.exponent = None

    def update_my_deriv(self, coefficient, variable, exponent):
        ''' docstring '''
        self.coefficient = coefficient
        self.variable = variable
        self.exponent = exponent

    def update_my_input(self):
        ''' docstring '''
        coefficient = int(input("enter a whole number for coefficient: "))
        variable = str(input("enter a letter for variable: "))
        exponent = int(input("enter a whole number for exponent: "))
        self.update_my_deriv(coefficient, variable, exponent)

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

my_deriv = MyDeriv()
my_deriv.update_my_input()
my_deriv.return_parent()
my_deriv.print_parent()
my_deriv.return_differenciation()
my_deriv.print_differenciation()

# End-of-file (EOF)
