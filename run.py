import importlib
tag_input_guide = ['1', 'input guide']
tag_run_input = ['2', 'run input']
tag_derivate_guide = ['3', 'derivate guide']
tag_run_derivate = ['4', 'run derivate']
tag_linear2p_guide = ['5', 'linear 2p equation guide']
tag_run_linerar2p = ['6', 'run linear 2p equation']
tag_exit = ['99', 'halt', 'exit', 'quit', 'stop', 'close']

loop_run = True
tag_application = None
my_polymonial = {

}

def run(tag_application):
        ''' docstring '''
        if tag_application in tag_input_guide:
            f = open("input_guide.txt")
            print(f.read())
            print("Hit Enter to continue...")
            input('')

        elif tag_application in tag_run_input:
            global my_polymonial
            my_polymonial.clear()
            from input_recognition import InputRecognition
            from polymonial_input import MyPolymonial
            input_recognition = InputRecognition()
            poly = MyPolymonial()
            poly.reset()
            input_recognition.all_index = []
            input_recognition.int_index = []
            input_recognition.var_index = []
            input_recognition.opr_index = []
            input_recognition.monomonial = ['+',]
            input_recognition.dict_index = 0
            input_recognition.my_dict = {}
            input_recognition.run_input()
            my_polymonial = input_recognition.my_dict
            print("this: "+ str(my_polymonial))
            print("Hit Enter to continue...")
            input('')

        elif tag_application in tag_derivate_guide:
            f = open("derivate_guide.txt")
            print(f.read())
            print("Hit Enter to continue...")
            input('')

        elif tag_application in tag_run_derivate:
            import derivate_coefficient
            importlib.reload(derivate_coefficient)
            print("Hit Enter to continue...")
            input('')

        elif tag_application in tag_linear2p_guide:
            f = open("linear_2p_guide.txt")
            print(f.read())
            print("Hit Enter to continue...")
            input('')

        elif tag_application in tag_run_linerar2p:
            import linear_2p_equation
            importlib.reload(linear_2p_equation)
            print("Hit Enter to continue...")
            input('')

        elif tag_application in tag_exit:
            print("Hit Enter to exit... ")
            input('')
            print("Exiting My Math Pilot")
            global loop_run
            loop_run = False
        else:
            print("There is no such application. please, try again.")
            print("Hit Enter to continue...")
            input('')

def initialize():
    ''' code '''
    while loop_run == True:
        print("--- Type the program you want to use: ---")
        print('')
        print('1: input guide')
        print('2: run input')
        print('3: derivate guide')
        print('4: run derivate')
        print('5: linear 2p equation guide')
        print('6: run linear 2p equation')
        tag_application = input("Run: ") 
        run(tag_application)

if __name__ == '__main__':
    print("--- My Math Pilot ver 1.0 ---")
    print("")
    initialize()

# End-of-file (EOF)
