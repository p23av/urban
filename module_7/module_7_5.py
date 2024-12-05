import os, time

directory = '.'
for root, dirs, files in os.walk(directory):
    # print(f'root - {root}')
    # print(f'dir - {dirs}')
    # print(f'files - {files}')
    for file in files:
        stat = os.stat(file)
        filepath = f'{root}/{file}'
        filetime = stat.st_mtime
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = stat.st_size
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')



# print(os.getcwd())
#
# if not os.path.exists('second'):
#     os.mkdir('second')
# os.chdir('second')
# print(f'{os.getcwd()}')
# # os.makedirs('third\\fourth') or r'string'
# print(os.listdir())
# for i, j ,k in os.walk('.'):
#     print(f'** {k}')
#     # print(os.stat(k[0]))