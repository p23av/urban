# nums = [1, 2, 3, 4, 5, 6, 7]
# a = (x**3 for x in nums)
# print(a)
# for i in a:
#     print(i)
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = [len(x[0]) - len(x[1]) for x in zip(first, second) if len(x[0]) != len(x[1])]
second_result = [len(first[x]) == len(second[x]) for x in range(len(first))]

print(list(first_result))
print(list(second_result))