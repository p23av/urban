def all_variants(text):
    n = len(text) + 1
    for len_ in range(1, n):
        for start in range(n - len_):
            end = start + len_
            yield text[start:end]

a = all_variants("abcd")
for i in a:
    print(i)

# def func_generator(n):
#     i = 0
#     while i != n:
#         yield i
#         i += 1
#
# obj = func_generator(10)
# print(obj)
#
# for i in obj:
#     print(i)