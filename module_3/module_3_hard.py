data_structure = [
  [1, 2, 3.3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
# data_structure = [1,2,3,4, 'sdfs', [6, 'qwert'], {5: 'asdqw', 'qw': 'ert'}]
# data_structure = {1: 'a', 'asd': 2}
# data_structure = {1, 'a', 2}

def calculate_structure_sum(data):
    counter = 0
    if data is None:
        print(data)
    if isinstance(data, str):
        return len(data)
    elif isinstance(data, int) or isinstance(data, float):
        return data
    elif isinstance(data, list) or isinstance(data, tuple):
        for item in data:
            counter += calculate_structure_sum(item)
        return counter
    elif isinstance(data, dict):
        return calculate_structure_sum(list(data.items()))
    elif isinstance(data, set):
        return calculate_structure_sum(list(data))
    return counter + calculate_structure_sum(data)

result = calculate_structure_sum(data_structure)
print(result)
