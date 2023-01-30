import math

def menu():
    print("vui lòng chọn trong 2 chức năng\n 1. Giải phương trình bậc 1 \n 2. Giải phương trình bậc 2")

def ptbac1(a,b):
    if a==0:
        if b==0:
            return "Phương trình có vô số nghiệm"
        return "Phương trình vô nghiệm"
    return "phương trình có một nghiệm duy nhất:\n x = {}".format(-b/a)
def ptbac2(a,b,c):
    if a == 0:
        return ptbac1(a,b)
    delta = b * b - 4 * a * c
    if delta > 0:
        x1 = float((-b + math.sqrt(delta)) / (2 * a))
        x2 = float((-b - math.sqrt(delta)) / (2 * a))
        return "Phuong trinh co hai nghiem phan biet la: \nx1 = {} \nx2 = {}".format(x1, x2)
    if delta == 0:
        x = -b / (2 * a)
        return "Phuong trinh co nghiem kep: \nx1 = x2 = {}".format(x)
    return "Phuong trinh vo nghiem"

menu()

chucnang = input()
if chucnang == '1':
    a,b = map(float,input().split())
    print(ptbac1(a,b))
elif chucnang == '2':
    a,b,c = map(float,input().split())
    print(ptbac2(a,b,c))
else:
    menu()
