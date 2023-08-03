"""Stepper I"""
def count(number):
    """print number"""
    for i in range(1, number + 1):
        print(i)
        i += 1

count(int(input()))
