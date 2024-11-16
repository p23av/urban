grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
grades_arithmetic = list(map(lambda x: sum(x) / len(x), grades))
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_sorted = sorted(list(students))
dict_ = dict(zip(students_sorted, grades_arithmetic))
print(dict_)