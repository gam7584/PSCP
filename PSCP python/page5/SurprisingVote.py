"""SurprisingVote"""
def surprising(total, max_num):
    """ห่างกัน 2 ถือว่าเซอร์ไพร"""
# first > second > third
    second = min(total - max_num, max_num)
    min_num = total - (max_num + second)
    if max_num - min_num <= 2:
        print("Not surprising")
    else:
        print("Surprising")
# print(max_num, second, min_num)

surprising(float(input()), float(input()))
