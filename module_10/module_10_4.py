import random
from queue import Queue
import time, threading

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

    def set_guest(self, guest):
        self.guest = guest

    def del_guest(self):
        self.guest = None

class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))

class Cafe:
    def __init__(self, *tables):
        self.tables = [*tables]
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for guest in [*guests]:
            for table in self.tables:
                if table.guest is None:
                    table.set_guest(guest)
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    break
            self.queue.put(guest)
            print(f'{guest.name} в очереди')


    def discuss_guests(self):

        flag = True
        while flag:
            if flag#self.queue.is_alive
                print(f'<имя гостя за текущим столом> покушал(-а) и ушёл(ушла)')
                print(f'Стол номер <номер стола> свободен')
                table.del_guest()
            elif not flag:
                guest = self.queue.get()
                table.set_guest(guest)
                print(f'<имя гостя из очереди> вышел(-ла) из очереди и сел(-а) за стол номер <номер стола>')






# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()


# def getter(queue):
#     while True:
#         time.sleep(1)
#         item = queue.get()
#         print(f'* {threading.current_thread()} // Взят элемент {item}')
#
# q = Queue(maxsize=10)
# thread1 = threading.Thread(target=getter, args=(q,), daemon=True)
# thread1.start()
# for i in range(10):
#     time.sleep(0.5)
#     q.put(i)
#     print(threading.current_thread(), i)
#
# # q.put(5)
# # print(q.get(timeout=2))
# # print('Конец очереди')
