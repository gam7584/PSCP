"""Circular II"""
def mosqito():
    """circular me and friend"""
    linex_me = float(input())
    liney_me = float(input())
    radius_me = float(input())
    linex_friend = float(input())
    liney_friend = float(input())
    radius_friend = float(input())
    # ระยะห่างระหว่างเครื่อง 2 เครื่อง
    distance = float((((linex_me - linex_friend)**2) + (liney_me - liney_friend)**2)**0.5)
    # ระยะห่างที่น้อยที่สุดโดยรัศมีการทำงานไม่ทับซ้อนกัน
    range_ = radius_friend + radius_me
    if range_ > distance:
        print("Yes")
    else:
        print("No")
mosqito()

