
tag_run_input = ['1', 'input']
tag_derivate_guide = ['2', 'derivate guide']
tag_count_coefficient = ['3', 'count coefficient']
tag_linerar_equation = ['4', 'count linear 2p equation']

tag_application = None
my_polymonial = {

}

print("Type the program you want to use:")
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
    else:
        print("try again")

tag_application = input("Run: ")
run(tag_application)

# End-of-file (EOF)
