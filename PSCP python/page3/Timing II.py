"""Timing II"""
def timing():
    """calulator time"""
    second = int(input())
    minutes = second // 60
    second = second % 60
    hours = minutes//60
    minutes = minutes % 60
    days = hours // 24
    hours = hours % 24
    # calculator
    if len(str(days)) > 4:
        print("ERR_:__:__:__")
    else:
        print("%04d:%02d:%02d:%02d"%(days, hours, minutes, second))

timing()
