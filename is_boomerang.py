def is_boomerang(p1,p2,p3):
    if abs(p1[0] - p2[0]) == abs(p1[1] - p2[1]) and abs(p2[0] - p3[0]) == abs(p2[1] - p3[1]):
        return False
    else: return True