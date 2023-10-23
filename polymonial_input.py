''' Following characters can be used '''
LEGAL_VAR = ['a', 'b', 'c', 'x', 'y', 'z']
LEGAL_OPR = ['+', '-', '*', '/', '^', 'sqrt']
LEGAL_INT = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

''' all things filtering messy input into organised libraries '''


class MyPolymonial:
    '''
    Each character is stored inside each list, in an
    'Excel manner'.
    See the flowchart for more details.
    '''
    def __init__(self):
        self.all_index = []
        self.int_index = []
        self.var_index = []
        self.opr_index = []

    def update_my_index(self, input_expression):
        ''' transfering user input to practical code '''
        self.input_expression = input_expression

    def update_my_expression(self, new_index):
        ''' Captured from user input in later code '''
        self.input_expression = new_index

    def update_my_input(self):
        ''' input source '''
        new_index = str(input("input: \n"))
        self.update_my_expression(new_index)

    def append_all_index(self):
        ''' Has to be done before verification '''
        self.all_index.clear()
        self.int_index.clear()
        self.var_index.clear()
        self.opr_index.clear()
        for i in self.input_expression:
            if i in LEGAL_INT or i in LEGAL_OPR or i in LEGAL_VAR:
                self.all_index.append(i)
            else:
                print(str(i) + " will be discarded")

    def verify_all_index(self):
        ''' Verification has to be done after append_all_index '''
        for i in self.all_index:
            if i in LEGAL_INT:
                self.int_index.append(int(i))
                self.var_index.append(None)
                self.opr_index.append(None)

            elif i in LEGAL_VAR:
                self.int_index.append(None)
                self.var_index.append(i)
                self.opr_index.append(None)

            elif i in LEGAL_OPR:
                self.int_index.append(None)
                self.var_index.append(None)
                self.opr_index.append(i)
            else:
                continue

    def return_all_index(self):
        '''
        Makes all_index accessible across
        functions and other Python files
        '''
        return (self.all_index)

    def return_int_index(self):
        '''
        Makes int_index accessible across
        functions and other Python files
        '''
        return (self.int_index)

    def return_var_index(self):
        '''
        Makes var_index accessible across
        functions and other Python files
        '''
        return (self.var_index)

    def return_opr_index(self):
        '''
        Makes opr_index accessible across
        functions and other Python files
        '''
        return (self.opr_index)

    def print_index(self):
        ''' console feedback '''
        print('polymonial_input all: ' + str(self.all_index))
        print('polymonial_input int: ' + str(self.int_index))
        print('polymonial_input var: ' + str(self.var_index))
        print('polymonial_input opr: ' + str(self.opr_index))

    def run(self):
        '''
        Bundle function that makes this
        Python file running for convenience
        '''
        self.update_my_input()
        self.append_all_index()
        self.verify_all_index()

    def reset(self):
        '''
        Clearing all index is neccessary for revisits
        '''
        self.all_index.clear()
        self.int_index.clear()
        self.var_index.clear()
        self.opr_index.clear()


if __name__ == '__main__':
    pass

# End-of-file (EOF)
