def count_primes(n):
    counter = 0
    for num in range(n):
        count = 0
        if num == 2 or num == 3:
            counter += 1
            continue
        if num == 1 or num % 2 == 0:
            continue
        ildiz = int(num ** 1 / 2)
        for i in range(3, ildiz + 1, 2):
            if num % i == 0:
                count += 1
        if count == 0:
            counter+=1
    return counter
print(count_primes(20))