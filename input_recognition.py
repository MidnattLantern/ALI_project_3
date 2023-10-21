from polymonial_input import MyPolymonial
my_polymonial = MyPolymonial()

class InputRecognition():
    ''' docstring '''
    def __init__(self):
        self.all_index = []
        self.int_index = []
        self.var_index = []
        self.opr_index = []
        # first is always positive
        self.monomonial = ['+',]
        self.dict_index = 0
        # reset this!
        self.my_dict = {

        }

    def print_all(self):
        ''' docstring '''
        for x in self.int_index:
            print('(input_recognition) '+ str(x))
        for y in self.var_index:
            print('(input_recognition) '+ str(y))
        for z in self.opr_index:
            print('(input_recognition) '+ str(z))

    def split(self):
        ''' docstring'''
        self.my_dict.update({
            self.dict_index: [''.join(self.monomonial)]
        })

    def generate_monomonial(self):
        ''' docstring '''
        # generating each monomonial
        for i, _ in enumerate(self.all_index):
            if self.int_index[i] != None:
                self.monomonial.append(str(self.int_index[i]))

            elif self.var_index[i] != None:
                self.monomonial.append(str(self.var_index[i]))

            elif self.opr_index[i] != None:
                if self.opr_index[i] == '^':
                    self.monomonial.append(str(self.opr_index[i]))

                else:
                    self.split()
                    self.dict_index += 1
                    self.monomonial.clear()
                    self.monomonial.append(str(self.opr_index[i]))

            # checking final index, this cannot be an elif !!
            if int(i+ 1) == int(len(self.all_index)):
                self.split()
                self.monomonial.append(str(self.opr_index[i]))

    def return_my_polymonial(self):
        ''' docstring '''
        return(self.my_dict)
    
    def print_my_polymonial(self):
        ''' docstring '''
        print('(input_recognition)'+ str(self.my_dict))

    def run_input(self):
        ''' test function '''
        self.my_dict.clear()
        print(self.my_dict)

        my_polymonial.update_my_input()
        my_polymonial.append_all_index()
        my_polymonial.verify_all_index()
        self.all_index = my_polymonial.return_all_index()
        self.int_index = my_polymonial.return_int_index()
        self.var_index = my_polymonial.return_var_index()
        self.opr_index = my_polymonial.return_opr_index()
        self.generate_monomonial()
        self.return_my_polymonial()
        self.print_my_polymonial()
        self.return_my_polymonial()

'''
input_recognition = InputRecognition()
input_recognition.run_input()

new_polynomial = MyPolymonial()
new_polynomial.run()

# recomended string
'''

if __name__ == '__main__':
    input_recognition = InputRecognition()
    input_recognition.run_input()
