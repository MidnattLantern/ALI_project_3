''' Following characters can be used '''
LEGAL_LETTERS_VAR = ['a', 'b', 'c', 'x', 'y', 'z']
LEGAL_LETTERS_OPERATORS = ['+', '-', '*', '/', '^', 'sqrt']
LEGAL_INTEGERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

''' all things filtering messy input into organised libraries '''
class MyPolymonial:
    ''' all_index and input_expresson may store illegal characters,
     but int_index, var_index, opr_index wont, and only those will
     be used for following steps '''
    def __init__(self, input_expression):
        # The "organised libraries"
        self.all_index = []
        self.int_index = []
        self.var_index = []
        self.opr_index = []
        self.input_expression = input_expression

    def update_input_expression(self, new_index):
        ''' Captured from user input in later code '''
        self.input_expression = new_index

    def append_all_index(self):
        ''' Has to be done before verification '''
        for i in self.input_expression:
            self.all_index.append(i)
            print(self.all_index)

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
                print(i + " is an operator")
                self.int_index.append(None)
                self.var_index.append(None)
                self.opr_index.append(i)
            else:
                print(i + ' is illegal and will be discarded')
                continue

    def print_index(self):
        ''' user's feedback '''
        print(self.all_index)
        print(self.int_index)
        print(self.var_index)
        print(self.opr_index)
        print(self.input_expression)

new_polinomial = MyPolymonial("")

new_polinomial.update_input_expression(str(input("input: ")))

new_polinomial.append_all_index()

new_polinomial.verify_all_index()

new_polinomial.print_index()

# End-of-file (EOF)
