def is_disarium_number(num):
    str_num = str(num)
    num_len = len(str_num)
    num_sum = 0
    for i in range(1, num_len + 1):
        num_sum += int(str_num[i-1]) ** i
    if num_sum == num:
        return True
    else: return False
print(is_disarium_number(135))