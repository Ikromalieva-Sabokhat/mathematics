text = "hi"
maketranss = str.maketrans(text[0],"s")
text = text.translate(maketranss)
print(text)
maketranss = str.maketrans(text[1],"p")
text = text.translate(maketranss)
print(text)
