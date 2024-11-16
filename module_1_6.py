my_dict = {
    'Alex': 1990,
    'Denis': 1950,
    'Max': 1930,
}
print(my_dict)
print(my_dict['Alex'])
print(my_dict.get('Artem'))
my_dict.update({'Elena': 1980, 'Natalia': 1970})
print(my_dict.pop('Denis'))
print(my_dict)

my_set = {1,1, 'str', '1', 'apple', 'str', False, (0,0,1)}
print(my_set)
my_set.add(77)
my_set.add(3.14)
my_set.discard('str')
print(my_set)