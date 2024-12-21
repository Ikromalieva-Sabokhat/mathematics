def binary_to_decimal(binary_str):
    decimal = 0
    power = 0
    for digit in reversed(binary_str):
        if digit not in {'0', '1'}:
            return "Noto'g'ri ikkilik son kiritildi."
        decimal += int(digit) * (2 ** power)
        power += 1
    return decimal
