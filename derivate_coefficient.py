''' docstring '''

class MyDeriv():
    '''
    Math terms recap: example 7x^5
    'monomial' is the entirety of 7x^5
    'coefficient" in this example is 7
    'variable' in this example is x
    'exponent' in this example is ^5
    'parent function' is the function before finding derivate,
    in this example 7x^5
    'differenciation' is the function after finding derivate,
    in this example 35x^4
    '''
    def __init__(self, coefficient, variable, exponent):
        self.coefficient = coefficient
        self.variable = variable
        self.exponent = exponent

    def parent_function(self):
        '''
        Returns the calculated parent, split as two rows due
        to length
        '''
        print_parent = f"{self.coefficient}{self.variable}^{self.exponent}"
        return f"parent function is: {print_parent}"

    def differenciation(self):
        '''
        Returns the calculated differenciation, split as three
        rows due to length
        '''
        print_differ_1 = f"{self.coefficient* self.exponent}"
        print_differ_2 = f"{self.variable}^{self.exponent- 1}"
        return f"differenciation is: {print_differ_1}{print_differ_2}"


COEFFICIENT_INPUT = int(input("enter a whole number for coefficient: "))
VARIABLE_INPUT = str(input("enter a letter for variable: "))
EXPONENT_INPUT = int(input("enter a whole number for exponent: "))

my_deriv = MyDeriv(COEFFICIENT_INPUT, VARIABLE_INPUT, EXPONENT_INPUT)
print(my_deriv.parent_function())
print(my_deriv.differenciation())

# End-of-file (EOF)
