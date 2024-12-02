from random import choice

# lambda
first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x == y, first, second)))

# замыкание
def get_advanced_writer(file_name):

    def write_everything(*data_set):
        file = open(file_name, 'a', encoding='utf-8')
        for data in [*data_set]:
            file.write(f'{data}\n')
        file.close()

    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Метод __call__
class MysticBall:

    def __init__(self, *words):
        self.words = [*words]

    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())

# def multiplier_v1(n):
#     if n == 2:
#         def multiplier(x):
#             return x * 2
#     elif n == 3:
#         def multiplier(x):
#             return x * 3
#     else:
#         raise Exception("Ya ne mogy cdelat' etot mnojitel'")
#     return multiplier
#
# def multiplier_v2(n):
#
#     def multiplier(x):
#         return x * n
#     return multiplier
#
# my_nums = [3, 1, 4, 5, 9, 2, 43]
# b_2 = multiplier_v2(5)
# print(list(map(b_2, my_nums)))
# # b_2 = multiplier_v1(2)
# # b_3 = multiplier_v1(3)
# # res = map(b_2, my_nums)
# # print(list(res))
# # # my_nums2 = [4, 6, 7, 8, 3, 5, 1]
# # # res = map(lambda x, y: x + y, my_nums, my_nums2)
# # # print(list(res))