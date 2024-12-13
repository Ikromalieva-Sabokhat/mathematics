def caesar_cipher(text, shift):
    new_text = ""
    for i in range(len(text)):
        kod = ord(text[i])
        yangi_kod = kod + shift
        farq = yangi_kod - 90
        if farq > 0:
            yangi_kod = 64 + farq
        yangi_harf = chr(yangi_kod)
        make_trans = str.maketrans(text[i], yangi_harf)
        new_text += text[i].translate(make_trans)
    return new_text
print(caesar_cipher("PYTHON",5))