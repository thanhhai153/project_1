#Nhap so do ba canh tu ban phim
#Su dung ham map() va float de ep kieu du lieu sang so thuc
print('vui lòng nhập số đo 3 cạnh của tam giác:')
try:
    a, b, c = map(float, input().split())

#Dung cau lenh re nhanh de kiem tra dieu kien
    if a+b>c and a+c>b and b+c>a:
#Neu dieu kien dung thi xuat thong bao
        print("{}, {}, {} la ba canh cua mot tam giac".format(a, b, c))
    else:
#Neu dieu kien sai thi xuat thong bao
        print("{}, {}, {} khong la ba canh cua mot tam giac".format(a, b, c))
except:
    print('có lỗi sảy ra')