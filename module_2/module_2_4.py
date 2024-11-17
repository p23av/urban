numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):
    # специально сделал доп условие, а не страрт в цикле с определённой позиции ( range(1, len(numbers)) )
    # т.к. в цикле перебираются индексы, а в условии проверяются значения
    if numbers[i] < 2:
        continue
    is_primes = True
    for j in range(2, numbers[i]):
        if numbers[i] % j == 0:
            is_primes = False
            break
    if is_primes:
        primes.append(numbers[i])
    else:
        not_primes.append((numbers[i]))

print(primes)
print(not_primes)