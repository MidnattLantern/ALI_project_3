''' docstring '''
LEGAL_LETTERS_VAR = ['a', 'b', 'c', 'x', 'y', 'z',]
LEGAL_LETTERS_OPERATORS = ['+', '-', '*', '/', '^', 'sqrt',]
LEGAL_INTEGERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

''' docstring '''
MY_STRING = []
INPUT_EXPRESSION = None


def update_my_string():
    ''' docstring '''
    print(MY_STRING)
    new_string = input(str("type your expression: "))
    new_string = new_string.replace(" ", "").lower()
    return new_string


INPUT_EXPRESSION = update_my_string()


def append_my_string():
    ''' docstring '''
    for i in INPUT_EXPRESSION:
        MY_STRING.append(i)
        print(MY_STRING)


def verify_my_string():
    for i in MY_STRING:
        print(i)
        if i in LEGAL_INTEGERS:
            print("integer")
        elif i in LEGAL_LETTERS_VAR:
            print("variable")
        elif i in LEGAL_LETTERS_OPERATORS:
            print("operator")
        else:
            print("illegal")


append_my_string()
verify_my_string()
verify_my_string()

# End-of-file (EOF)
