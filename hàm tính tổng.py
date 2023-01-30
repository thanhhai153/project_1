def tinhtong(*args):
    tong = 0
    for i in args:
        tong += i
    return tong
print("1 + 2 +3 = {}".format(tinhtong(1, 2,3)))

