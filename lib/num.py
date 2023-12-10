# Checks if two numbers are positive, if they are prints out true, if not prints pout false
def two_are_positive(a, b, c):
    if (c > 0 and b > 0 and a > 0):
        return False
    elif (a > 0 and b > 0) or (a > 0 and c > 0) or (c > 0 and b > 0):
        return True
    return False

    result = two_are_positive(5, 6, -9)

    print (result)