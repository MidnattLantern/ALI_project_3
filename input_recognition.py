all_index = [2, 5, 'x', '^', 5,'+','7', '-']
int_index = [2, 5, None, None, 5, None, '7', None]
var_index = [None, None, 'x', None, None, None, None, None]
opr_index = [None, None, None, '^', None, '+', None, '-']
filter = []

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
        dict_index: [''.join(filter)]
    })
    print(my_dict)

print('------')
# the , _ excludes the value
for i, _ in enumerate(all_index):
    if int_index[i] != None:
        filter.append(str(int_index[i]))
    if var_index[i] != None:
        filter.append(str(var_index[i]))
    if opr_index[i] != None:
        if opr_index[i] == '^':
            filter.append(str(opr_index[i]))
        else:
            split()
            dict_index += 1
            filter.clear()
            filter.append(str(opr_index[i]))
