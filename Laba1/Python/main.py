def sect (x1, y1, x2, y2):
    if y1 == y2:
        s = "The section is parallel to OX"
    elif x1 == x2:
        s = "The section is parallel to OY"
    elif x1 == 0 and x2 == 0:
        s = "The section is belong to OX"
    elif y1 == 0 and y2 == 0:
        s = "The section is belong to OY"
    elif x1 != x2 and y1 != y2:
        s = "The section is not belong nor OX, nor OY"
    return (s)
print(sect(0, 0, 0, 6))
