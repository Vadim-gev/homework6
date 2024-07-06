my_dict = {'Vadim': 1987, 'Oleg': 1991, 'Egor': 1995}
print(my_dict)
print(my_dict.get('Vadim'))
print(my_dict.get('Vasya'))
my_dict.update({'Nikita': 1992, 'Roman': 1985})
a = my_dict.pop('Nikita')
print(a)
print(my_dict)

my_set = {1, 2, 1, 1, 3, 4, 2, 'a', 'b', 'a', 'c'}
print(my_set)
my_set.add(5)
my_set.add('e')
my_set.remove(3)
print(my_set)
