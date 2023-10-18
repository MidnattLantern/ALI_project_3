all_index = [2, 5, 'x', '^', 5,'+','7', '+', '2', '-']
int_index = [2, 5, None, None, 5, None, 7, None, 2, None]
var_index = [None, None, 'x', None, None, None, None, None, None, None]
opr_index = [None, None, None, '^', None, '+', None, '+', None, '-']
monomonial = ['+',]

dict_index = 0

my_dict = {

}

def print_all():
    for x in int_index:
        print(x)
    print('------')
    for y in var_index:
        print(y)
    print('------')
    for z in opr_index:
        print(z)
print_all()

def split():
    my_dict.update({
        dict_index: [''.join(monomonial)]
    })
    print(my_dict)

print('------')
# generating each monomonial
for i, _ in enumerate(all_index):
    print(i+ 1)
    if int_index[i] != None:
        monomonial.append(str(int_index[i]))

    elif var_index[i] != None:
        monomonial.append(str(var_index[i]))

    elif opr_index[i] != None:
        if opr_index[i] == '^':
            monomonial.append(str(opr_index[i]))

        else:
            split()
            dict_index += 1
            monomonial.clear()
            monomonial.append(str(opr_index[i]))

    # cannot be elif !!
    if int(i+ 1) == int(len(all_index)):
        split()
        monomonial.append(str(opr_index[i]))

print(my_dict)