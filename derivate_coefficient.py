
class MyDeriv():
    """
    Math terms recap: example 7x^5
    'monomial' is the entirety of 7x^5
    'coefficient" in this example is 7
    'variable' in this example is x
    'exponent' in this example is ^5
    'parent function' is the function before finding derivate, in this example 7x^5
    'differenciation' is the function after finding derivate, in this example 35x^4
    """
    def __init__(self, coefficient, variable, exponent):
        self.coefficient = coefficient
        self.variable = variable
        self.exponent = exponent

    def parent_function(self):
        return f"parent function is: {self.coefficient}{self.variable}^{self.exponent}"
    def differenciation(self):
        return f"differenciation is: {self.coefficient * self.exponent}{self.variable}^{self.exponent - 1}"

coefficient_input = int(input("enter a whole number for coefficient: "))
variable_input = str(input("enter a letter for variable: "))
exponent_input = int(input("enter a whole number for exponent: "))

my_deriv = MyDeriv(coefficient_input, variable_input, exponent_input)
print(my_deriv.parent_function())
print(my_deriv.differenciation())