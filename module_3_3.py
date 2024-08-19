def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = ['Urban', 3, True]
values_dict = {'a': values_list[0], 'b': values_list[1], 'c': values_list[2]}

print_params(*values_dict)
print_params(**values_dict)

values_list_2 = [[True], 'Университет', 12]
print(values_list_2, 42)


