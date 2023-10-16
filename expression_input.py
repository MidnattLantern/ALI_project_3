'''docstring'''
SLICED_EXPRESSION = []
SLICED_EXPRESSION_INT_TARGET = []
SLICED_EXPRESSION_STR_TARGET = []
SLICED_EXPRESSION_type = []
MONOMIAL_DICTIONARY = {}

# edit of expression as string
print("Note: integer following ^ will be an exponent")
INPUT_EXPRESSION = str(input("Enter expression: "))
# filtering out CAPITAL and spaces
INPUT_EXPRESSION = INPUT_EXPRESSION.replace(" ", "").lower()
print("Expression: "+ INPUT_EXPRESSION)

# SLICED_EXPRESSION
for i in INPUT_EXPRESSION:
    SLICED_EXPRESSION.append(i)

print("------")
for i in SLICED_EXPRESSION:
    try:
        print(int(i))
        SLICED_EXPRESSION_INT_TARGET.append(i)
        SLICED_EXPRESSION_STR_TARGET.append(None)
    except TypeError:
        print(i+ " is not an integer")
        SLICED_EXPRESSION_STR_TARGET.append(i)
        SLICED_EXPRESSION_INT_TARGET.append(None)
print("------")

print("------")
print("all: "+ str(SLICED_EXPRESSION))
#print(range(len(SLICED_EXPRESSION)))
print("int: "+ str(SLICED_EXPRESSION_INT_TARGET))
#print(range(len(SLICED_EXPRESSION_INT_TARGET)))
print("str: "+ str(SLICED_EXPRESSION_STR_TARGET))
#print(range(len(SLICED_EXPRESSION_STR_TARGET)))
print("------")

# Identifying strings and integers using libraries
print("------")
for i in enumerate(SLICED_EXPRESSION):
    if SLICED_EXPRESSION[i] == SLICED_EXPRESSION_INT_TARGET[i]:
        print(str(SLICED_EXPRESSION[i])+ " is an integer")
        SLICED_EXPRESSION_type.append(int)
    elif SLICED_EXPRESSION[i] == SLICED_EXPRESSION_STR_TARGET[i]:
        print(str(SLICED_EXPRESSION[i])+ " is a string")
        SLICED_EXPRESSION_type.append(str)
    else:
        print("error: unable to identify integer or string for"+ str(SLICED_EXPRESSION[i]))
print("------")


print("------")
WRITE_MONOMIAL = ""
MONOMIAL_INDEX = 0
for x in enumerate(SLICED_EXPRESSION_type):
    if SLICED_EXPRESSION_type[x] == int:
        WRITE_MONOMIAL += SLICED_EXPRESSION[x]
    elif SLICED_EXPRESSION_type[x] == str:
        # Detecting operators
        if SLICED_EXPRESSION_STR_TARGET[x] not in ["^", "+", "-", "*", "/", "sqrt"]:
            WRITE_MONOMIAL += SLICED_EXPRESSION[x]
            # Create monomial, reset WRITE_MONOMIAL, then move on to the next
            MONOMIAL_DICTIONARY[MONOMIAL_INDEX] = WRITE_MONOMIAL
            MONOMIAL_INDEX += 1
            WRITE_MONOMIAL = ""
    # Detecting when reaching the final input character
    if x == len(SLICED_EXPRESSION[x]):
        print("final object")
        if SLICED_EXPRESSION_type[x] == int:
            print("final object is an integer")
print("total indexes: "+ str(len(SLICED_EXPRESSION)))
print(MONOMIAL_DICTIONARY)

print("------")

# End-of-file (EOF)
