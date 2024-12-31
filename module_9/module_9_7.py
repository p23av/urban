def is_prime(func):
    def wrapper(*args, **kwargs):
        sum = func(*args, **kwargs)
        flag_prime = False
        answer = ['Простое', 'Составное']
        if sum == 2:
            print(answer[0])
            return sum
        for i in range(2, sum // 2 + 1):
            if sum % i == 0:
                flag_prime = True
        if flag_prime:
            print(answer[1])
        else:
            print(answer[0])
        return sum
    return wrapper

@is_prime
def sum_three(one, two, three):
    return one + two + three

result = sum_three(2,3,6,)
print(result)





# def uppercase(func):
#     # original_result = func()
#     # modified_result = original_result.upper()
#     # return modified_result
#     def wrapper():
#         original_result = func()
#         modified_result = original_result.upper()
#         return modified_result
#     return wrapper
#
# @uppercase
# def greet():
#     return 'Herro!'
#
# print(greet)