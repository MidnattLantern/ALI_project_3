
tag_run_input = ['1', 'input']
tag_derivate_guide = ['2', 'derivate guide']
tag_count_coefficient = ['3', 'count coefficient']
tag_linerar_equation = ['4', 'count linear 2p equation']

tag_application = None
my_polymonial = {

}

print("--- Type the program you want to use: ---")
print("1: input")
print("2: derivate guide")
print("3: count countefficient")
print("4: count linear 2p equation")

def run(tag_application):
    ''' docstring '''
    if tag_application in tag_run_input:
        global my_polymonial
        from input_recognition import InputRecognition
        new_polynomial = InputRecognition()
        new_polynomial.run_input()
        my_polymonial = new_polynomial.return_my_polymonial()
        print(my_polymonial)
    elif tag_application in tag_derivate_guide:
        f = open('derivate_guide.txt', encoding='utf-8')
        lines = f.read()
        f.close()
        print(lines)
    elif tag_application in tag_count_coefficient:
        from derivate_coefficient import MyDeriv
        my_deriv = MyDeriv()
        my_deriv.update_my_input()
        my_deriv.return_parent()
        my_deriv.print_parent()
        my_deriv.return_differenciation()
        my_deriv.print_differenciation()
    elif tag_application in tag_linerar_equation:
        from linear_2p_equation import myLinear2pEquation
        my_2p = myLinear2pEquation()
        my_2p.update_my_input()
        my_2p.calculate_2p()
    else:
        print("try again")

tag_application = input("Run: ") 
run(tag_application)

# End-of-file (EOF)
