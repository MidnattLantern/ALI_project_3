''' docstring '''

run_input = ['1', 'input']
derivate_guide = ['2', 'derivate_guide', 'derivate guide', 'derivate help']

APPLICATION = None

print("Type the program you want to use:")
print("1: input")
print("2: derivate guide")

def run(APPLICATION):
    ''' docstring '''
    if APPLICATION in run_input:
        from expression_input import MyPolymonial
        new_polinomial = MyPolymonial("")
        new_polinomial.update_input_expression(str(input("input: ")))
        new_polinomial.append_all_index()
        new_polinomial.verify_all_index()
        new_polinomial.print_index()
    elif APPLICATION in derivate_guide:
        f = open('derivate_guide.txt', encoding='utf-8')
        lines = f.read()
        f.close()
        print(lines)
    else:
        print("try again")

APPLICATION = input("Run: ")
run(APPLICATION)

# End-of-file (EOF)
