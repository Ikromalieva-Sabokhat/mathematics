import math
def find_factorions(start, end):
    def factorial(a):
        fac = 1
        for i in range(1, a + 1):
            fac *= i
        return fac
    sonlar = []
    for n in range(start, end + 1):
        son_list = [int(son) for son in str(n)]
        summ = 0
        for son in son_list:
            summ += factorial(son)
        if summ == n:
            sonlar.append(n)
    return sonlar
print(find_factorions(1, 500))