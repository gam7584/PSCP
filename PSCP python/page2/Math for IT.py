"""MFIT"""
def main():
    """MFIT"""
    import math as m
    radius = float(input())
    area = (m.pi * (radius**2))
    circumference = (2*(m.pi*radius))
    print("Area: %.3f " %area)
    print("Circumference: %.3f" %circumference)
main()
