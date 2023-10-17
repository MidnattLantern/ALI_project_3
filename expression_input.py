''' docstring '''
LEGAL_LETTERS_VAR = ['a', 'b', 'c', 'x', 'y', 'z']
LEGAL_LETTERS_OPERATORS = ['+', '-', '*', '/', '^', 'sqrt']
LEGAL_INTEGERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

''' docstring '''
class MyPolymonial:
    ''' docstring '''
    def __init__(self, input_expression):
        # comment
        self.all_index = []
        self.int_index = []
        self.var_index = []
        self.opr_index = []
        self.input_expression = input_expression

    def update_input_expression(self, new_index):
        ''' docstring '''
        self.input_expression = new_index

    def print_index(self):
        print(self.all_index)
        print(self.int_index)
        print(self.var_index)
        print(self.opr_index)
        print(self.input_expression)

new_polinomial = MyPolymonial("test")

new_polinomial.update_input_expression(str(input("input: ")))

print(new_polinomial.input_expression)


# End-of-file (EOF)

'''
def append_all_index():

    for i in input_expression:
        all_index.append(i)
        print(all_index)


def verify_all_index():

    for i in all_index:
        if i in LEGAL_INTEGERS:
            print(i + " is an integer")
            int_index.append(int(i))
            var_index.append(None)
            opr_index.append(None)
        elif i in LEGAL_LETTERS_VAR:
            print(i + " is a variable")
            int_index.append(None)
            var_index.append(i)
            opr_index.append(None)
        elif i in LEGAL_LETTERS_OPERATORS:
            print(i + " is an operator")
            int_index.append(None)
            var_index.append(None)
            opr_index.append(i)
        else:
            print(i + " is illegal and will be discarded")
            continue
    print("Integer index: " + str(int_index))
    print("Variable index: " + str(var_index))
    print("Operator index: " + str(opr_index))
'''



# End-of-file (EOF)
