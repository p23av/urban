from math import pi, sqrt

class Figure:
    sides_count = 0

    def __init__(self):
        self.__sides = None
        self.__color = []
        self.filled = True

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        is_valid = True
        for color in [r, g, b]:
            if isinstance(color, int) and 0 <= color <= 255:
                continue
            else:
                is_valid = False
                break
        # print(is_valid)
        return is_valid

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]


    def __is_valid_sides(self, *sides):
        flag_is_valid = len(*sides) == len(self.__sides)
        for side in [*sides]:
            if isinstance(side, int) and side > 0:
                continue
            else:
                flag_is_valid = False
                break
        if flag_is_valid:
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        len_ = 0
        for i in self.__sides:
            len_ += i
        return len_

    def set_sides(self, *new_sides):
        if self.__sides is None or len([*new_sides]) == len(self.__sides):
            self.__sides = [*new_sides]

class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, side):
        super().__init__()
        self.__radius = side / (2 * pi)
        self.set_sides(side)

class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, side1, side2, side3):
        super().__init__()
        self.set_sides(side1, side2, side3)

    def get_square(self):
        a, b, c = self.get_sides()
        p = (a + b + c) / 2
        return sqrt(p * (p - a) * (p - b) * (p - c))

class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, side):
        super().__init__()
        self.set_sides(*([side] * 12))
        self.set_color(*__color)

    def get_volume(self):
        return self.get_sides()[0] ** 3






circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

triangle1 = Triangle((222, 35, 130), 4,13,15)
print(triangle1.get_square())