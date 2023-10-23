from polymonial_input import MyPolymonial
my_polymonial = MyPolymonial()


class InputRecognition():
    '''
    Each character is stored inside each list, in an
    'Excel manner'.
    See the flowchart for more details.
    "my_dict" aka "my_polynomial"
    '''
    def __init__(self):
        self.all_index = []
        self.int_index = []
        self.var_index = []
        self.opr_index = []
        self.monomonial = ['+', ]
        self.dict_index = 0
        self.my_dict = {

        }

    def print_all(self):
        '''
        Console feedback to support development
        '''
        for x in self.int_index:
            print('(input_recognition) ' + str(x))
        for y in self.var_index:
            print('(input_recognition) ' + str(y))
        for z in self.opr_index:
            print('(input_recognition) ' + str(z))

    def split(self):
        '''
        Recognizing the begining and the end of each monomial
        '''
        self.my_dict.update({
            self.dict_index: [''.join(self.monomonial)]
        })

    def generate_monomonial(self):
        '''
        After recognizing, it's time to generate a
        monomial.
        The last if statement checks the last letter,
        because the last letter needs special treatment.
        '''
        for i, _ in enumerate(self.all_index):
            if self.int_index[i] is not None:
                self.monomonial.append(str(self.int_index[i]))

            elif self.var_index[i] is not None:
                self.monomonial.append(str(self.var_index[i]))

            elif self.opr_index[i] is not None:
                if self.opr_index[i] == '^':
                    self.monomonial.append(str(self.opr_index[i]))

                else:
                    self.split()
                    self.dict_index += 1
                    self.monomonial.clear()
                    self.monomonial.append(str(self.opr_index[i]))

            if int(i + 1) == int(len(self.all_index)):
                self.split()
                self.monomonial.append(str(self.opr_index[i]))

    def return_my_polymonial(self):
        '''
        To make the polynomial stored here
        accessable outside this document
        '''
        return (self.my_dict)

    def print_my_polymonial(self):
        '''
        console feedback if appropriate for
        user or developer
        '''

    def run_input(self):
        '''
        Bundle function that lets you run all
        things necessary with jjust one command.
        '''
        self.my_dict.clear()

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


if __name__ == '__main__':
    input_recognition = InputRecognition()
    input_recognition.run_input()

# End-of-file (EOF)
