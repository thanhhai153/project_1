# input và định dạng về float, sau đó tách từng số ra với split
a, b, c = map(float, input().split())
#Dung cau lenh re nhanh de kiem tra dieu kien
if a+b>c and a+c>b and b+c>a:
#Neu dieu kien dung thi xuat thong bao
#print("{}, {}, {} la ba canh cua mot tam giac".format(a, b, c))
    if a*a == ( b*b +c*c) or b*b == (a*a+c*c) or c*c==(a*a+b*b):
        loaitamgiac='vuông'
    elif a*a > ( b*b +c*c) or b*b > (a*a+c*c) or c*c > (a*a+b*b):
        loaitamgiac='tù'
    elif a==c and a==b:
        loaitamgiac='đều'
    elif a==c or a==b or b==c:
        loaitamgiac='cân'
    else:
        loaitamgiac = 'nhọn'
    print("{}, {}, {}  la ba canh cua mot tam giac {}".format(a, b, c,loaitamgiac))        
else:
#Neu dieu kien sai thi xuat thong bao
    print("{}, {}, {} khong la ba canh cua mot tam giac".format(a, b, c))