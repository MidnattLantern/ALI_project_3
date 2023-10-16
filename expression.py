''' docstring '''


class MyInput():
    '''
    docstring
    '''
    def __init__(self, coefficient, variable, exponent):
        self.coefficient = coefficient
        self.variable = variable
        self.exponent = exponent

        # statement
    def expression(self):
        '''
        docstring
        '''
        print_my_coefficient = f"{self.coefficient}"
        print_my_variable = f"{self.variable}"
        print_my_exponent = f"{self.exponent}"
        return f"expression: {print_my_coefficient}{print_my_variable}{print_my_exponent}"


COEFFICIENT_INPUT = int(input("enter a whole number for coefficient: "))
VARIABLE_INPUT = str(input("enter a letter for variable: "))
EXPONENT_INPUT = int(input("enter a whole number for exponent: "))

my_input = MyInput(COEFFICIENT_INPUT, VARIABLE_INPUT, EXPONENT_INPUT)
print(my_input.expression())

# End-of-file (EOF)
