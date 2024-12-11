

class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError("шаг не может быть равен 0")
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = self.start


    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if self.step > 0 and (not self.pointer > self.stop) or self.step < 0 and (not self.pointer < self.stop):
            result_ = self.pointer
            self.pointer += self.step
            return result_
        else:
            raise StopIteration()


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()


# class Iter:
#     def __init__(self):
#         self.first = 'Первый элемент'
#         self.second = 'Втолрой элемент'
#         self.third ='Третий элемент'
#         self.i = 0
#
#     def __iter__(self):
#         self.i = 0
#         return self
#
#     def __next__(self):
#         self.i +=1
#         if self.i == 1:
#             return self.first
#         if self.i == 2:
#             return self.second
#         if self.i == 3:
#             return self.third
#         if self.i == 4:
#             return 'Подсчет закончен'
#         raise StopIteration()
#
# obj = Iter()
# print(obj)
# for value in obj:
#     print(value)