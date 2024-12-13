def is_harshad(n):
    raqamlar = [int(i) for i in str(n)]
    print(raqamlar)
    if n % sum(raqamlar) == 0:
        return True
    return False
print(is_harshad(19))