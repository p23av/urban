from modules.sortfunc import *

data_1 = list(map(int, input('Введите числа через пробел: ').split()))
data_2 = list(map(int, input('Введите числа через пробел: ').split()))

print(bubble_sort(data_1))
print(selection_sort(data_2))