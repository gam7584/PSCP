"""Brick Bridge"""
def bridge():
    """Brick Bridge"""
    brick_a = int(input())
    brick_b = int(input())
    goal = int(input())
    brick_use = goal//5 #จำนวนbrickที่ต้องใช้มากที่สุดที่เป็นไปได้
    # length_brick = brick_use * 5 #ระยะที่ต้องใช้

    if brick_use > brick_b:#b_b = ใช้เมื่อb_b < b_u
        #เปรียบเทียบจำนวนก้อนที่ใช้กับก้อนใหญ่ ถ้ามากกว่า ให้เอาระยะสะพานลบกับระยะbrick_b
        #(brick_bคือจำนวนอิฐก้อนใหญ่ที่มี)
        left_length = goal - (brick_b*5)#เราต้องใช้ก้อนใหญ่ให้หมดก่อน
        corndog_(brick_a, left_length)
    else:
        left_length = goal - (brick_use*5)#ใช้b_uในกรณีนี้
        corndog_(brick_a, left_length)

def corndog_(brick_a, left_length):#compare brick_a is enough to bulid
    """condition"""
    if brick_a >= left_length:
        print(left_length)
    else:
        print(-1)

bridge()
