"""Stepper II"""
def step(num_1, num_2):
    """num_1 to num_2"""
    if num_1 > num_2:
        for i in range(num_1, num_2-1, -1):
            print(i)
    elif num_1 < num_2:
        for i in range(num_1, num_2+1):
            print(i)
    elif num_1 == num_2:
        print(num_1)

step(int(input()), int(input()))
