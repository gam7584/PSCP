y1, m1, d1 = [int(e) for e in input().split()]
y2, m2, d2 = [int(e) for e in input().split()]
# e คือ ตัวแปร
if y2 > y1:
    print("1")
elif y2 < y1:
    print("2")
elif y2 == y1:
    if m2 > m1:
        print("1")
    elif m2 < m1:
        print("2")
    elif m2 == m1:
        if d2 > d1:
            print("1")
        elif d2 < d1:
            print("2")
        elif d2 == d1:
            print("equal")
