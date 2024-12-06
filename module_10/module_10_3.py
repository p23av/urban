import threading, random, time

class Bank:
    def __init__(self, balance = 0):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            increase_value = random.randint(50, 500)
            self.balance += increase_value
            print(f'Пополнение: {increase_value}. Баланс: {self.balance}')
            time.sleep(0.001)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

    def take(self):
        for i in range(100):
            decrease_value = random.randint(50, 500)
            print(f'Запрос на {decrease_value}')
            if self.balance >= decrease_value:
                self.balance -= decrease_value
                print(f'Снятие: {decrease_value}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

# counter = 0
# lock = threading.Lock()
#
# def increment(name):
#     global counter
#     lock.acquire()
#     for i in range(1000):
#         counter += 1
#         print(name, counter)
#     lock.release()
#
# def decrement(name):
#     global counter
#     with lock:
#         for i in range(1000):
#             counter -= 1
#             print(name, counter)
#
# thread1 = threading.Thread(target=increment, args=('thread1',))
# thread2 = threading.Thread(target=decrement, args=('thread2',))
# thread3 = threading.Thread(target=increment, args=('thread3',))
# thread4 = threading.Thread(target=decrement, args=('thread4',))
# thread1.start()
# thread3.start()
# thread2.start()
# thread4.start()
