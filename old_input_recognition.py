from polymonial_input import MyPolymonial

all_index = []
int_index = []
var_index = []
opr_index = []

new_polynomial = MyPolymonial()
new_polynomial.update_my_input()
new_polynomial.append_all_index()
new_polynomial.verify_all_index()
new_polynomial.print_index()

all_index = new_polynomial.return_all_index()
int_index = new_polynomial.return_int_index()
var_index = new_polynomial.return_var_index()
opr_index = new_polynomial.return_opr_index()
print("test: "+ str(all_index))
print("test: "+ str(int_index))
print("test: "+ str(var_index))
print("test: "+ str(opr_index))


# first is always positive
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

    # checking final index, this cannot be an elif !!
    if int(i+ 1) == int(len(all_index)):
        split()
        monomonial.append(str(opr_index[i]))

print("my_dict: "+ str(my_dict))