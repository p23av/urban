import io
from pprint import pprint

def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'a', encoding='utf-8')
    i = 0
    for string in strings:
        i += 1
        pos_key = (i, file.tell())
        pos_value = string
        file.write(f'{string}\n')
        strings_positions[pos_key] = pos_value
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

# name = 'sample2.txt'
# file = open(name, 'r', encoding='utf-8')
# print(file.writable())
# print(file.readable())
# print(file.seekable())
# print(file.tell())
# pprint(file.read())
# print(file.tell())
# file.close()