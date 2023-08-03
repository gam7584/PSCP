"""BMI"""
def main():
    """BMI"""
    name = input()
    weight = float(input())
    tall = float(input())
    result = (weight/((tall / 100)**2))
    return name, result
def many():
    """BMI"""
    name_1, result_1 = main()
    name_2, result_2 = main()
    name_3, result_3 = main()
    name_4, result_4 = main()
    name_5, result_5 = main()
    #print(name ,%.2f "'s = " , result)
    print("%s's  BMI = " %name_1 + "%.2f" %result_1)
    print("%s's  BMI = " %name_2 + "%.2f" %result_2)
    print("%s's  BMI = " %name_3 + "%.2f" %result_3)
    print("%s's  BMI = " %name_4 + "%.2f" %result_4)
    print("%s's  BMI = " %name_5 + "%.2f" %result_5)

many()
