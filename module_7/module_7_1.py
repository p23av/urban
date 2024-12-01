from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        prods = file.read()
        file.close()
        return prods

    def add(self, *products):
        self_prods = self.get_products()
        file = open(self.__file_name, 'a')
        for prod in [*products]:
            if prod.name in self_prods:
                print(f'Продукт {prod.name} уже есть в магазине')
            else:
                file.write(f'{prod}\n')
        file.close()

# Product('Potato', 50.0, 'Vagetables')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
# -----------------------



# name = 'sample.txt'
# name = 'sample2.txt'
# file = open(name, 'r') # r - read, w - write, a - append
# file = open(name, 'w') # r - read, w - write, a - append
# file = open(name, 'a') # r - read, w - write, a - append
# file.write('\nhello2')
# file.close()



# print(ord('a'))
#
# s = ''
# for c in [104, 101, 108, 108, 111]:
#     s += chr(c)
# print(s)