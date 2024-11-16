immutable_var = (1, '2', False, [0,2])
print(immutable_var)
# immutable_var[0] = True # Ошибка - кортеж неизменяем
mutable_list = [1,2,3]
mutable_list[0] = False
mutable_list[1] = True
mutable_list[2] = 'str'
print(mutable_list)