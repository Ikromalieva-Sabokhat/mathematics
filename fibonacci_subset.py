def fibonacci_subset(numbers):
    def is_fibonacci(n): # n = 5
        fibonacci = [0, 1]
        son = 0
        i = 0
        while son < n:
            son = fibonacci[i] + fibonacci[i + 1]
            fibonacci.append(son)
            i += 1
        if n in fibonacci:
            return True
        else: return False
    fibo_sonlar = []
    for son in numbers:
        if is_fibonacci(son):
            fibo_sonlar.append(son)
    return fibo_sonlar
print(fibonacci_subset([10, 11, 12]))


def is_not_fibonacci(n):  # n = 5
    fibonacci = [0, 1]
    son = 0
    i = 0
    while son < n:
        son = fibonacci[i] + fibonacci[i + 1]
        fibonacci.append(son)
        i += 1
    if n in fibonacci:
        return False
    else:
        return True
print(is_not_fibonacci(11))