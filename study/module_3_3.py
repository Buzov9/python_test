def print_params(a=1, b='str', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [1.5, 2, 'word']
values_dict = {'a': False, 'b': 11, 'c': '1c'}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [4.5, 'False']
print_params(*values_list_2, 42)
