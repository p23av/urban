from random import random


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        if dz < 0:
            print("It's too deep, i can't dive :(")
            return
        self._cords = [dx * self.speed, dy * self.speed, dz * self.speed]

    def get_cords(self):
        x, y, z = self._cords
        print(f'X: {x}, Y: {y}, Z: {z}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        random_ = round(random() * 4)
        print(f"Here are(is) {random_} eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] += int((-dz) * (self.speed / 2))

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    sound = "Click-click-click"

    def speak(self):
        print(self.sound)

db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()


# class Human:
#
#     def __init__(self, name, gr):
#         self.name = name
#         self.gr = gr
#
#     def say_hi(self):
#         print(f'hi from {self.name}, {self.gr}')
#
# class Group:
#     num = 1
#     def __init__(self, gr):
#         self.gr = gr
#
# class Student(Human, Group):
#     def __init__(self, name, place, gr):
#         super().__init__(name, gr)
#         self.place = place
#         self.say_hi()
#         self.gr = gr
#
# human = Human('alex', 'piton 1')
# student = Student('max', 'urban', 'piton 1')
# print(human.name)
# print(dir(student))