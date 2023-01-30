#dùngslpit để tách ra và ép về số thực float
a, pheptinh, b= input().split()
a=float(a)
b=float(b)
#biến lưu kết quả biểu thức
ketqua=None

if pheptinh=='+':
    ketqua= a+b
elif pheptinh=='-':
    ketqua=a-b
elif pheptinh=='x':
    ketqua= a*b
elif pheptinh== ':':
    if b==0:
        Print('không hợp lệ')
    else:
        ketqua=a/b
#Neu bien ketQua khac None thi chung to bieu thuc hop le
if ketqua != None:
   #In ra man hinh bieu thuc va ket qua
   print("{} {} {} = {}".format(a, pheptinh, b, ketqua))