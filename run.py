
tag_input_guide = ['1', 'input guide']
tag_run_input = ['2', 'run input']
tag_derivate_guide = ['3', 'derivate guide']
tag_run_derivate = ['4', 'run derivate']
tag_linear2p_guide = ['5', 'linear 2p equation guide']
tag_run_linerar2p = ['6', 'run linear 2p equation']
tag_exit = ['halt', 'exit', 'quit', 'stop']

loop_run = True
tag_application = None
my_polymonial = {

}

def run(tag_application):
        ''' docstring '''
        if tag_application in tag_input_guide:
            print("app 1")
        elif tag_application in tag_run_input:
            print("app 2")
        elif tag_application in tag_derivate_guide:
            print("app 3")
        elif tag_application in tag_run_derivate:
            print("app 4")
        elif tag_application in tag_linear2p_guide:
            print("app 5")
        elif tag_application in tag_run_linerar2p:
            print("app 6")
        elif tag_application in tag_exit:
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
        print('5', 'linear 2p equation guide')
        print('6', 'run linear 2p equation')
        tag_application = input("Run: ") 
        run(tag_application)

if __name__ == '__main__':
    print("--- My Math Pilot ver 1.0 ---")
    print("")
    initialize()

# End-of-file (EOF)
