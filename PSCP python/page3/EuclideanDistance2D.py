"""EuclideanDistance2D"""
def main():
    """EuclideanDistance2D"""
    num_q1 = float(input())
    num_q2 = float(input())
    num_p1 = float(input())
    num_p2 = float(input())
    result = ((((num_q1-num_p1)**2) + ((num_q2-num_p2)**2))**0.5)
    print(result)
main()
