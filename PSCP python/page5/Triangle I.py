"""Triangle I"""
def triangle():
    """find yes or no"""
    var_1 = float(input())
    var_2 = float(input())
    var_3 = float(input())

    if -0.01 <= (var_1**2) - (var_2**2 + var_3**2) <= 0.01:
        print("Yes")
    elif -0.01 <= (var_2**2) - (var_1**2 + var_3**2) <= 0.01:
        print("Yes")
    elif -0.01 <= (var_3**2) - (var_1**2 + var_2**2) <= 0.01:
        print("Yes")
    else:
        print("No")

triangle()
