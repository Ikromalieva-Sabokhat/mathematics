def binary_toggle(n):
    ikkilik = bin(n)[2:]
    almashgan = str(ikkilik)
    yangi_str = ""
    for i in almashgan:
        if i == "0":
            yangi_str += "1"
        elif i == "1":
            yangi_str += "0"
    return int(yangi_str, 2)


print(binary_toggle(5))
