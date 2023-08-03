"""SumOfNumber"""
def sumofnumber():
    """input -1 and print sum"""
    while True:
        number = int(input())
        listt = []
        listt.extend(number)
        if number == -1:
            break
        print(listt)
sumofnumber()



# n = int(input())
# list2 = []
# for i in range(n):
#     list2.append(int(input()))
# sum = 0
# for i in list2:
#     sum = sum + i
#     print(sum)
