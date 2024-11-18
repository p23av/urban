def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()

print_params(b = 25)
print_params(c = [1,2,3])

values_list = [1, 'apple', 5.5]
values_dict = {'a': True, 'b': 'orange', 'c': 4.4}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [3.3, 'table']
print_params(*values_list_2, 42)