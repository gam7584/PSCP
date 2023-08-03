"""Circular I"""
def mosqito():
    """mosqito"""
    radx_me = float(input())
    rady_me = float(input())
    radius = float(input())
    radx_mosqito = float(input())
    rady_mosqito = float(input())
    result = (((radx_me - radx_mosqito)**2 + (rady_me - rady_mosqito)**2)**0.5)
    if result <= radius:
        print("Yes")
    elif result > radius:
        print("No")

mosqito()
