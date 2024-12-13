def extract_nums(s):
    sonlar = ""
    for i in s:
        if i.isnumeric():
            sonlar+=i
    if len(sonlar) > 0:
        return sonlar
    else: return None
