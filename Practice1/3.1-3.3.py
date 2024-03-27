def multiply12(a):
    # a = 2
    b = a + a  # 4
    c = b + b  # 8
    d = c + c  # 16
    ans = c + d  # 24
    return ans


print("3.1: 2 * 12 = " + str(multiply12(2)))


def multiply16(a):
    # a = 1
    b = a + a  # 2
    c = b + b  # 4
    d = c + c  # 8
    ans = d + d  # 16
    return ans


print("3.2: 2 * 16 = " + str(multiply16(2)))


def multiply15(a):
    # a = 1
    b = a + a  # 2
    c = b + b  # 4
    d = c + c  # 8
    ans = d - (a - d)
    return ans


print("3.3: 2 * 15 = " + str(multiply15(2)))
