def min_(list_):
    return min(list_)
def max_(list_):
    return max(list_)
def len_(list_):
    return len(list_)
def sum_(list_):
    return sum(list_)
def sorted_(list_):
    return sorted(list_)

def apply_all_func(int_list, *functions):
    results = {}
    for function in functions:
        print(function.__name__)
        results[function.__name__] = function(int_list)
    return results

print(apply_all_func([6, 20, 15, 9], max_, min_))
print(apply_all_func([6, 20, 15, 9], len_, sum_, sorted_))