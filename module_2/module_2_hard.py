import random
first_num = random.choice(range(3, 20))
print(first_num)
second_num = ''
for i in range(1,20):
    for j in range(i + 1, 20):
        if first_num % (i + j) == 0:
            second_num += str(i) + str(j)
result = int(second_num)
print(result)