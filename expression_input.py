# user input will automatically be proccessed to a readable equation, regardless how messy and nonselsical it may be
"""
- any variable, such as x y z will always have
 a coefficient and an exponent,
if neither is given, they'll automatically be assigned as 1
- any non integer will be automatically seperated
"""

# "libraries" or "library"
sliced_expression = []
sliced_expression_int_target = []
sliced_expression_str_target = []
sliced_expression_type = []
monomial_dictionary = {}

# edit of expression as string
print("Note: integer following ^ will be an exponent")
input_expression = str(input("Enter expression: "))
# filtering out CAPITAL and spaces
input_expression = input_expression.replace(" ", "").lower()
print("Expression: "+ input_expression)

# sliced_expression
for i in input_expression:
    sliced_expression.append(i)

print("------")
for i in sliced_expression:
    try:
        print(int(i))
        sliced_expression_int_target.append(i)
        sliced_expression_str_target.append(None)
    except:
        print(i+ " is not an integer")
        sliced_expression_str_target.append(i)
        sliced_expression_int_target.append(None)
print("------")

print("------")
print("all: "+ str(sliced_expression))
#print(range(len(sliced_expression)))
print("int: "+ str(sliced_expression_int_target))
#print(range(len(sliced_expression_int_target)))
print("str: "+ str(sliced_expression_str_target))
#print(range(len(sliced_expression_str_target)))
print("------")

# Identifying strings and integers using libraries
print("------")
for i in range(len(sliced_expression)):
    if sliced_expression[i] == sliced_expression_int_target[i]:
        print(str(sliced_expression[i])+ " is an integer")
        sliced_expression_type.append(int)
    elif sliced_expression[i] == sliced_expression_str_target[i]:
        print(str(sliced_expression[i])+ " is a string")
        sliced_expression_type.append(str)
    else:
        print("error: unable to identify integer or string for"+ str(sliced_expression[i]))
print("------")

'''
- An expression, such as 12x, would in this case be:
1 as index [0], 2 as index [1], and x as index[2]
- Values may have more than one digit, so the next
index will be appended to the string.
- Variables in math are always single, so if the next
or first or next index is a string, a monomial will be
generated using the given values up until that point.
- monomial_index keeps track how many monomials there
should exist.
'''
print("------")
write_monomial = ""
monomial_index = 0
for x in range(len(sliced_expression_type)):
    if sliced_expression_type[x] == int:
        write_monomial += sliced_expression[x]
    elif sliced_expression_type[x] == str:
        # Detecting operators
        if sliced_expression_str_target[x] not in ["^", "+", "-", "*", "/", "sqrt"]:
            write_monomial += sliced_expression[x]
            # Create monomial, reset write_monomial, then move on to the next
            monomial_dictionary[monomial_index] = write_monomial
            monomial_index += 1
            write_monomial = ""
    # Detecting when reaching the final input character
    if x == len(sliced_expression[x]):
        print("final object")
        if sliced_expression_type[x] == int:
            print("final object is an integer")
print("total indexes: "+ str(len(sliced_expression)))
print(monomial_dictionary)

print("------")