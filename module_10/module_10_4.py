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
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        # print('> start', self.name)
        time.sleep(random.randint(3, 10))
        # print('>> finish', self.name)

class Cafe:
    def __init__(self, *tables):
        self.tables = [*tables]
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for guest in [*guests]:
            flag_closed_table = True
            for table in self.tables:
                if table.guest is None:
                    table.set_guest(guest)
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    flag_closed_table = False
                    break
            if flag_closed_table:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')
        # print('end arrival')

    def discuss_guests(self):
        while self.queue.empty() == False or len(list(filter(lambda table: not table.guest is None, self.tables))) > 0:
            # time.sleep(1)
            # print('**', [(table.number, 'None' if table.guest is None else table.guest.name) for table in self.tables], '*', '|', self.queue.qsize())
            # print('**', [table.guest.name for table in closed_tables], '*', '|', self.queue.qsize())
            for table in self.tables:
                is_closed_table = table.guest is None
                if is_closed_table == False and table.guest.is_alive() == False:
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.del_guest()
                elif self.queue.empty() == False and table.guest is None:
                    guest = self.queue.get()
                    table.set_guest(guest)
                    print(f'{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    guest.start()
                    # print('**', [(table.number, 'None' if table.guest is None else table.guest.name) for table in
                    #                self.tables])
        # print(closed_tables, self.queue.qsize())

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
