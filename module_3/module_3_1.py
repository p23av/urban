calls = 0
def count_calls():
    global calls
    calls += 1
    # print(calls)
def string_info(str_):
    length = len(str_)
    upper = str_.upper()
    lower = str_.lower()
    tuple_ = (length, upper, lower)
    count_calls()
    return tuple_
def is_contains(str_, list_):
    str_ = str_.lower()
    for i in range(len(list_)):
        list_[i] = list_[i].lower()
    is_contain = False
    if str_ in list_:
        is_contain = True
    count_calls()
    return is_contain

print(string_info('asdDDasd'))
print(string_info('Capybara'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)