def anagramic_difference(numbers):
    son = [int(son) for son in str(numbers)]
    max_son = max(son)
    min_son = min(son)
    max_index = son.index(max_son)
    min_index = son.index(min_son)
    for i in range(3):
        if i!=max_index and i != min_index:
            orta_son = son[i]
    return int(str(max_son) + str(orta_son) + str(min_son)) - int(str(min_son) + str(orta_son) + str(max_son))
