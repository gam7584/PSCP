"""Largest Number"""
def compare(var_1, var_2):
    """Largest Number"""
    if var_1 > var_2:
        return var_1
    return var_2


def largesttt():
    """what the lagrest number"""
    num_1 = input()
    num_2 = input()
    num_3 = input()

    largest = num_1 + num_2 + num_3
    largest = compare(num_1 + num_2 + num_3, largest)
    largest = compare(num_1 + num_3 + num_2, largest)
    largest = compare(num_2 + num_1 + num_3, largest)
    largest = compare(num_2 + num_3 + num_1, largest)
    largest = compare(num_3 + num_1 + num_2, largest)
    largest = compare(num_3 + num_2 + num_1, largest)
    print(largest)

largesttt()
