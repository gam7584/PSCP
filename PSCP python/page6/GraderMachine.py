"""GraderMachine"""
def machine(start, stop):
    for num in range(start, stop):
        num += 1
        if num % 2 == 0:
            print(num, end="")



machine(int(input()), int(input()))
