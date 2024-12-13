def is_factorial_prime(num):
    if num == 2 or num == 3:
        return True
    if num == 1 or num % 2 == 0:
        return False
    ildiz = int(num ** 1 / 2)
    for i in range(3, ildiz + 1, 2):
        if num % i == 0:
            return False
    factorial = 1
    i = 4
    while True:
        for i in range(2, i):
            factorial *= i
        if num == factorial + 1 or num == factorial - 1:
            return True
        elif factorial - num > 1:
            return False
        else:
            continue
        i += 1
