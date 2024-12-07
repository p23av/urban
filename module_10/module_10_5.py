import multiprocessing, time, threading

def read_info(name):
    all_data = []
    file = open(name, 'r', encoding='utf-8')
    flag = True
    while flag:
        line = file.readline()
        if line == '':
            flag = False
        else:
            all_data.append(line)
    file.close()

filenames = [f'./file {number}.txt' for number in range(1, 5)]

linear_time_start = time.time()
for filename in filenames:
    read_info(filename)
linear_time_end = time.time()
print(f'linear time: {linear_time_end - linear_time_start}')# linear time: 10.486566543579102

# thread_time_start = time.time()
# thread1 = threading.Thread(target=read_info, args=(filenames[0],))
# thread2 = threading.Thread(target=read_info, args=(filenames[1],))
# thread3 = threading.Thread(target=read_info, args=(filenames[2],))
# thread4 = threading.Thread(target=read_info, args=(filenames[3],))
# thread1.start()
# thread2.start()
# thread3.start()
# thread4.start()
# thread1.join()
# thread2.join()
# thread3.join()
# thread4.join()
# thread_time_end = time.time()
# print(f'thread time: {thread_time_end - thread_time_start}')# thread time: 10.196865320205688

# if __name__ == '__main__':
#     process_time_start = time.time()
#     with multiprocessing.Pool(processes=4) as pool:
#         pool.map(read_info, filenames)
#     process_time_end = time.time()
#     print(f'process time: {process_time_end - process_time_start}')#process time: 4.408844709396362
