''' docstring '''

tag_run_input = ['1', 'input']
tag_derivate_guide = ['2', 'derivate guide']
tag_count_coefficient = ['3', 'count coefficient']
tag_linerar_equation = ['4', 'count linear 2p equation']

TAG_APPLICATION = None

print("Type the program you want to use:")
print("1: input")
print("2: derivate guide")
print("3: count countefficient")
print("4: count linear 2p equation")

def run(TAG_APPLICATION):
    ''' docstring '''
    if TAG_APPLICATION in tag_run_input:
        from polymonial_input import MyPolymonial
        new_polinomial = MyPolymonial("")
        new_polinomial.update_input_expression(str(input("input: ")))
        new_polinomial.append_all_index()
        new_polinomial.verify_all_index()
        new_polinomial.print_index()
    elif TAG_APPLICATION in tag_derivate_guide:
        f = open('derivate_guide.txt', encoding='utf-8')
        lines = f.read()
        f.close()
        print(lines)
    elif TAG_APPLICATION in tag_count_coefficient:
        from derivate_coefficient import MyDeriv
        COEFFICIENT_INPUT = int(input("enter a whole number for coefficient: "))
        VARIABLE_INPUT = str(input("enter a letter for variable: "))
        EXPONENT_INPUT = int(input("enter a whole number for exponent: "))
        my_deriv = MyDeriv(COEFFICIENT_INPUT, VARIABLE_INPUT, EXPONENT_INPUT)
        print(my_deriv.parent_function())
        print(my_deriv.differenciation())
    elif TAG_APPLICATION in tag_linerar_equation:
        from linear_2p_equation import myLinear2pEquation
        my_2p = myLinear2pEquation()
        my_2p.update_input()
        my_2p.calculate_2p()
        my_2p.print_2p()
    else:
        print("try again")

TAG_APPLICATION = input("Run: ")
run(TAG_APPLICATION)

# End-of-file (EOF)
