''' docstring '''
class MyPolymonial:
    ''' docstring '''
    def __init__(self):
        # comment
        self.coefficient_dict = {'coefficient_0': None, 'coefficient_1': None,}
        self.variable_dict = {'variable_0': None, 'variable_1': None,}
        self.exponent_dict = {'exponent_0': None, 'exponent_1': None,}

    def update_coefficient_dict(self, new_data):
        ''' docstring '''
        self.coefficient_dict.update(new_data)

    def update_variable_dict(self, new_data):
        ''' docstring '''
        self.variable_dict.update(new_data)

    def update_exponent_dict(self, new_data):
        ''' docstring '''
        self.exponent_dict.update(new_data)

    def print_variables(self):
        ''' docstring '''
        print(self.coefficient_dict)
        print(self.variable_dict)
        print(self.exponent_dict)

new_polinomial = MyPolymonial()
new_polinomial.print_variables()
new_polinomial.update_coefficient_dict({'coefficient_0': 5})
new_polinomial.print_variables()

# End-of-file (EOF)
