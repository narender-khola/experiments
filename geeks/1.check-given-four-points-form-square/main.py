def distanceSqure(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def isSquare(p1, p2, p3, p4):
    d2 = distanceSqure(p1, p2)
    d3 = distanceSqure(p1, p3)
    d4 = distanceSqure(p1, p4)

    if d2==d3 and 2*d2==d4:
        d5 = distanceSqure(p4, p2)
        d6 = distanceSqure(p4, p3)
        return (d5==d6) and (d5==d2)

    if d2==d4 and 2*d2==d3:
        d5 = distanceSqure(p3, p2)
        d6 = distanceSqure(p3, p4)
        return (d5==d6) and (d5==d2)

    if d4==d3 and 2*d4==d2:
        d5 = distanceSqure(p2, p4)
        d6 = distanceSqure(p2, p3)
        return (d5==d6) and (d5==d4)

    return False

p1 = (20, 10)
p2 = (10, 20)
p3 = (20, 20)
p4 = (10, 10)
print isSquare(p1, p2, p3, p4)
