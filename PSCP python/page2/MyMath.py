"""MyMath"""
def equation():
    """what is this"""
    import math as m
    upper = (m.sin(m.radians(90))) + ((m.sin(m.radians(60))**2))
    under = (m.cos(m.radians(245**2))) + (m.cos(m.radians(45+135)))
    print(upper/under)
    print((m.factorial(16)) * (m.factorial(4)) / (m.factorial(8)))
    print((15+25)/(((25-12)**2)+((12-15)**2))**0.5)
    print(m.log(1234**4, 10))
    upper_1 = (m.log(4234, 5) + (m.log(8191, 2)) + (71*m.log(156154, 10)))
    under_1 = (m.log(777, 7))-(m.log(888, 8))-(m.log(999, 9))
    print(upper_1 / under_1)

equation()
