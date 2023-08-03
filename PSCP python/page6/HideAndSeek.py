"""HideAndSeek"""
def loop(start, stop, step):
    """num step"""
    for i in range(start, stop, step):
        print(i)
        i += 1

loop(int(input()), int(input()), int(input()))
