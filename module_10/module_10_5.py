import multiprocessing, time, threading

def read_info(name):
    all_data = []
    file = open(name, 'r', encoding='utf-8')
    file.readline()
    # readline

filenames = [f'./file {number}' for number in range(1, 5)]

main_time_start = time.time()
for filename in filenames:
    thread = threading.Thread(target=read_info, args=(filename,))
    thread.start()
    thread.join()
main_time_end = time.time()
print(f'thread time: {main_time_end - main_time_start}')

if __name__ == '__main__':
    process1 = multiprocessing.Process(target=first_worker, args=(10,))
    process1.start()


# counter = 0
#
# def first_worker(n):
#     global counter
#     for i in range(n):
#         counter += 1
#         time.sleep(1)
#     print(f'Первый рабочий изменил значение счётчика {counter}')
#
# def second_worker(n):
#     global counter
#     for i in range(n):
#         counter += 1
#         time.sleep(1)
#     print(f'Второй рабочий изменил значение счётчика {counter}')
#
# if __name__ == '__main__':
#     process1 = multiprocessing.Process(target=first_worker, args=(10,))
#     process2 = multiprocessing.Process(target=second_worker, args=(5,))
#     process1.start()
#     process2.start()

# thread1 = threading.Thread(target=first_worker, args=(10,))
# thread2 = threading.Thread(target=second_worker, args=(5,))
# thread1.start()
# thread2.start()
