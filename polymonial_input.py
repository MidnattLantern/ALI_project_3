''' Following characters can be used '''
LEGAL_LETTERS_VAR = ['a', 'b', 'c', 'x', 'y', 'z']
LEGAL_LETTERS_OPERATORS = ['+', '-', '*', '/', '^', 'sqrt']
LEGAL_INTEGERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

''' all things filtering messy input into organised libraries '''
class MyPolymonial:
    ''' all_index and input_expresson may store illegal characters,
     but int_index, var_index, opr_index wont, and only those will
     be used for following steps '''
    def __init__(self):
        # The "organised libraries"
        self.all_index = []
        self.int_index = []
        self.var_index = []
        self.opr_index = []

    def update_my_index(self, input_expression):
        ''' docstring '''
        self.input_expression = input_expression

    def update_my_expression(self, new_index):
        ''' Captured from user input in later code '''
        self.input_expression = new_index

    def update_my_input(self):
        ''' docstring '''
        new_index = str(input("input: "))
        self.update_my_expression(new_index)

    def append_all_index(self):
        ''' Has to be done before verification '''
        for i in self.input_expression:
            # how to shorten?
            if i in LEGAL_INTEGERS or i in LEGAL_LETTERS_OPERATORS or i in LEGAL_LETTERS_VAR:
                self.all_index.append(i)
                print('test: '+ str(self.all_index))
            else:
                print(str(i)+ " will be discarded")

    def verify_all_index(self):
        ''' Verification has to be done after append_all_index '''
        for i in self.all_index:
            if i in LEGAL_INTEGERS:
                print(i + ' is an integer')
                self.int_index.append(int(i))
                self.var_index.append(None)
                self.opr_index.append(None)

            elif i in LEGAL_LETTERS_VAR:
                print(i + ' is a variable')
                self.int_index.append(None)
                self.var_index.append(i)
                self.opr_index.append(None)


            elif i in LEGAL_LETTERS_OPERATORS:
                print(i + ' is an operator')
                self.int_index.append(None)
                self.var_index.append(None)
                self.opr_index.append(i)
            else:
                print(i + ' is illegal and will be discarded')
                continue

    def return_all_index(self):
        ''' docstring '''
        return(self.all_index)
    
    def return_int_index(self):
        ''' docstring '''
        return(self.int_index)
    
    def return_var_index(self):
        ''' docstring '''
        return(self.var_index)
    
    def return_opr_index(self):
        ''' docstring '''
        return(self.opr_index)

    def print_index(self):
        ''' user's feedback '''
        print('all: '+ str(self.all_index))
        print('int: '+ str(self.int_index))
        print('var: '+ str(self.var_index))
        print('opr: '+ str(self.opr_index))

'''
new_polynomial = MyPolymonial()
new_polynomial.update_my_input()
new_polynomial.append_all_index()
new_polynomial.verify_all_index()
new_polynomial.print_index()
'''

# End-of-file (EOF)
