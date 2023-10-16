''' docstring '''
LEGAL_LETTERS_VAR = ['a', 'b', 'c', 'x', 'y', 'z']
LEGAL_LETTERS_OPERATORS = ['+', '-', '*', '/', '^', 'sqrt']
LEGAL_INTEGERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

''' docstring '''
ALL_INDEX = []
INT_INDEX = []
VAR_INDEX = []
OPR_INDEX = []
INPUT_EXPRESSION = None


def update_all_index():
    ''' docstring '''
    print(ALL_INDEX)
    new_string = input(str("type your expression: "))
    new_string = new_string.replace(" ", "").lower()
    return new_string


INPUT_EXPRESSION = update_all_index()


def append_all_index():
    ''' docstring '''
    for i in INPUT_EXPRESSION:
        ALL_INDEX.append(i)
        print(ALL_INDEX)


def verify_all_index():
    ''' docstring '''
    for i in ALL_INDEX:
        if i in LEGAL_INTEGERS:
            print(i + " is an integer")
            INT_INDEX.append(int(i))
            VAR_INDEX.append(None)
            OPR_INDEX.append(None)
        elif i in LEGAL_LETTERS_VAR:
            print(i + " is a variable")
            INT_INDEX.append(None)
            VAR_INDEX.append(i)
            OPR_INDEX.append(None)
        elif i in LEGAL_LETTERS_OPERATORS:
            print(i + " is an operator")
            INT_INDEX.append(None)
            VAR_INDEX.append(None)
            OPR_INDEX.append(i)
        else:
            print(i + " is illegal and will be discarded")
            continue
    print("Integer index: " + str(INT_INDEX))
    print("Variable index: " + str(VAR_INDEX))
    print("Operator index: " + str(OPR_INDEX))


append_all_index()
verify_all_index()

# End-of-file (EOF)
