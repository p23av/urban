import threading, time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        x = 100
        day = 0
        print(f'{self.name}, на нас напали!')
        while x > 0:
            time.sleep(1)
            x -= self.power
            day += 1
            print(f'{self.name} сражается {day} дня(дней), осталось {x} воинов.')
        print(f'{self.name} одержал победу спустя {day} дней(дня)!')

# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')

# class MyThread(threading.Thread):
#     def __init__(self, name, counter, delay):
#         threading.Thread.__init__(self)
#         self.name = name
#         self.counter = counter
#         self.delay = delay
#
#     def timer(self, name, counter, delay):
#         while counter:
#             time.sleep(delay)
#             print(f'{name} {time.ctime()}')
#             counter -= 1
#
#     def run(self):
#         print(f'поток {self.name} запущен')
#         self.timer(self.name, self.counter, self.delay)
#         print(f'поток {self.name} завершен')
#
# thread1 = MyThread('thrd1', 5, 0.5)
# thread2 = MyThread('thrd2', 3, 0.3)
# thread1.start()
# thread2.start()
