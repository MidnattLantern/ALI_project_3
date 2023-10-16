''' docstring '''
LEGAL_LETTERS_VAR = ['a', 'b', 'c', 'x', 'y', 'z', '(', ')']
LEGAL_LETTERS_OPERATORS = ['+', '-', '*', '/', '^', 'sqrt']

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

append_my_string()

# End-of-file (EOF)
