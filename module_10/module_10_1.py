import threading, time

main_time_start = time.time()
def write_words(word_count, file_name):
    file = open(file_name, 'a', encoding='utf-8')
    for i in range(word_count):
        time.sleep(0.01)
        file.write(f'Какое-то слово № {i}\n')
    print(f'Завершилась запись в файл {file_name}')

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
main_time_end = time.time()
print(f'Работа потоков: {main_time_end - main_time_start} секунд')

thread_time_start = time.time()
thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()

thread_time_end = time.time()
print(f'Работа потоков: {thread_time_end - thread_time_start} секунд')

# def func1():
#     for i in range(10):
#         time.sleep(1)
#         print(i, threading.current_thread())
#
# def func2(x):
#     for i in range(10):
#         time.sleep(1)
#         print(i, threading.current_thread())
#
# thread = threading.Thread(target=func2, args=(1,), daemon=True)
# thread.start()
# func1()