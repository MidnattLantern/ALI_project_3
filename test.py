all_index = [2, 5, 'x', '^', 5,'+','7']
int_index = [2, 5, None, None, 5, None, '7']
var_index = [None, None, 'x', None, None, None, None]
opr_index = [None, None, None, '^', None, '+', None]

my_dict = {
    0: [0],
}

print(my_dict)

for i in range(8):
    my_dict.update({
        i: [i]
    })
    print(my_dict)