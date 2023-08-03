"""FoodGrade I"""
def chicken(i, count):
    """read comment"""
    #recursive function to get input 24 times and call function "compare_weight" to check condition
    if i <= 24:
        weight = int(input())
        count = compare_weight(weight, count)
        chicken(i+1, count)
    else:
        print(count)

def compare_weight(weight, count):
    """check condition and return value to the funtion "compare_weight" """
    if weight >= 50 and weight <= 70:
        return count + 1
    else:
        return count

chicken(1, 0)
