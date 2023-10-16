''' docstring '''
class MyVariable:
    ''' docstring '''
    def __init__(self):
        # comment
        self.var1_dict = {'coefficient': None, 'variable': None, 'exponent': None,}
        self.var2_dict = {'coefficient': None, 'variable': None, 'exponent': None,}
        self.var3_dict = {'coefficient': None, 'variable': None, 'exponent': None,}

    def update_dict1(self, new_data):
        ''' docstring '''
        self.var1_dict.update(new_data)
    
    def update_dict2(self, new_data):
        ''' docstring '''
        self.var2_dict.update(new_data)
    
    def update_dict3(self, new_data):
        ''' docstring '''
        self.var3_dict.update(new_data)

    def print_variables(self):
        ''' docstring '''
        print(self.var1_dict)
        print(self.var2_dict)
        print(self.var3_dict)

new_instance = MyVariable()
new_instance.print_variables()
new_instance.update_dict1({'coefficient': 2, 'variable': 'X', 'exponent': 4})
new_instance.print_variables()