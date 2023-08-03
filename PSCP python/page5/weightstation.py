"""trucky"""
def car():
    """trucky"""
    avg = float(input())
    weight_1 = float(input())
    weight_2 = float(input())
    weight_3 = float(input())
    weight_4 = (avg * 4) - (weight_1 + weight_2 + weight_3)
    all_weight = weight_1 + weight_2 + weight_3 + weight_4
    plus = avg + (avg/2)
    minus = avg - (avg/2)
    if all_weight > 15000:
        print("Overweight")

    elif minus > weight_1 or weight_1 > plus\
    or minus > weight_2 or weight_2 > plus\
    or minus > weight_3 or weight_3 > plus\
    or minus > weight_4 or weight_4 > plus:
        print("Unbalance")

    elif minus > weight_1 or weight_1 > plus\
    or minus > weight_2 or weight_2 > plus\
    or minus > weight_3 or weight_3 > plus\
    or minus > weight_4 or weight_4 > plus\
    and all_weight > 15000:
        print("Overweight")

    else:
        print("Pass %.2f"%weight_4)

car()
