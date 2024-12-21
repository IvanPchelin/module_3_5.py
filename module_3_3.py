def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print("--------------------")
print_params(b=25)
print_params(c=[1, 2, 3])
values_list = (1304, True, "Parametr")
print("--------------------")
print_params(*values_list)
values_dict = {'a': 1, 'b': 2, 'c': 3}
print_params(**values_dict)
print("--------------------")
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)



