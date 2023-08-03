"""CompositeFunction"""
def fun(xor):
    """CompositeFunction"""
    return 2*xor
def gun(xor):
    """CompositeFunction"""
    return (xor/2)+1
def main():
    """d"""
    call = int(input())
    print("%.2f"%(fun(gun(call))))
    print("%.2f"%(gun(fun(call))))
main()
