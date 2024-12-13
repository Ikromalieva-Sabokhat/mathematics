def merge_words(word1, word2):
    i = -1
    j = 1
    k = 0
    stop = min(len(word1), len(word2))
    while stop >= k:
        if word1[i:] == word2[:j]:
            bir_xil = word1[i:]
        i -= 1
        j += 1
        k += 1
    return word1[:len(word1) - len(bir_xil)] + bir_xil + word2[len(bir_xil):]

print(merge_words("python", "online"))
