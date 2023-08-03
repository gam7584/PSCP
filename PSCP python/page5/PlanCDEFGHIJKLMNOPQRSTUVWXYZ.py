"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
def set_number():
    """class of number"""
    option = input()
    num_1 = float(input())
    num_2 = float(input())
    num_3 = float(input())
    if option == "Ascend":
        less_to_most(num_1, num_2, num_3)
    elif option == "Descend":
        most_to_less(num_3, num_2, num_1)

def less_to_most(num_1, num_2, num_3):
    """less to most number"""
    # 1
    if num_1 >= num_2 >= num_3:
        print("%.2f, %.2f, %.2f"%(num_3, num_2, num_1))
    elif num_1 >= num_3 >= num_2:
        print("%.2f, %.2f, %.2f"%(num_2, num_3, num_1))
    # 2
    elif num_2 >= num_1 >= num_3:
        print("%.2f, %.2f, %.2f"%(num_3, num_1, num_2))
    elif num_2 >= num_3 >= num_1:
        print("%.2f, %.2f, %.2f"%(num_1, num_3, num_2))
    # 3
    elif num_3 >= num_1 >= num_2:
        print("%.2f, %.2f, %.2f"%(num_2, num_1, num_3))
    elif num_3 >= num_2 >= num_1:
        print("%.2f, %.2f, %.2f"%(num_1, num_2, num_3))

def most_to_less(num_1, num_2, num_3):
    """most to less number"""
    # 1
    if num_1 >= num_2 >= num_3:
        print("%.2f, %.2f, %.2f"%(num_1, num_2, num_3))
    elif num_1 >= num_3 >= num_2:
        print("%.2f, %.2f, %.2f"%(num_1, num_3, num_2))
    # 2
    elif num_2 >= num_1 >= num_3:
        print("%.2f, %.2f, %.2f"%(num_2, num_1, num_3))
    elif num_2 >= num_3 >= num_1:
        print("%.2f, %.2f, %.2f"%(num_2, num_3, num_1))
    # 3
    elif num_3 >= num_1 >= num_2:
        print("%.2f, %.2f, %.2f"%(num_3, num_1, num_2))
    elif num_3 >= num_2 >= num_1:
        print("%.2f, %.2f, %.2f"%(num_3, num_2, num_1))

set_number()
