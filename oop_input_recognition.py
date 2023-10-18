
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
        self.my_dict = {

        }

    def print_all(self):
        ''' docstring '''
        for x in self.int_index:
            print(x)
        print('------')
        for y in self.var_index:
            print(y)
        print('------')
        for z in self.opr_index:
            print(z)

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