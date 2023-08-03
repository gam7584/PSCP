# """Rectangle"""
# def squre_area(high,wide):
#     """Rectangle"""
#     area =  high*wide
# def perimeter(high,wide):
#     """Rectangle"""
#     return (high*2) + (wide*2)
# def answer():
#     """Rectangle"""
#     var_1 = int(input())
#     var_2 = int(input())
#     print(squre_area)
#     # print(var_1)
# answer()

# """Rectangle"""
# def main():
#     """Rectangle"""
#     high = int(input())
#     wide = int(input())
#     area = high*wide
#     perimeter = (high*2)+(wide*2)
#     print(area)
#     print(perimeter)
# main()

"""Rectangle"""
# def output():
#     """print out"""
#     width = int(input())
#     hight = int(input())
#     cal(width, hight)

# def cal(w, h):
#     """calculate"""
#     print(w * h)
#     print((w*2) + (h *2))

# output()

def main():
    width = int(input())
    hight = int(input())
    print(area(width, hight))
    print(line(width, hight))
    
def area(w, h):
    #return => area(paramiter) = result
    result = w*h
    return result


def line(w, h):
    result = (w*2) + (h*2)
    return result

main()