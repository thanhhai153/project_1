#Nhap so A tu ban phim va chuyen sang kieu so thuc
soA = float(input())

#Nhap so B tu ban phim va chuyen sang kieu so nguyen
soB = int(input())

#Dung ham format de dinh dang chuoi dau ra
print('dùng hàm format:{0:.{1}f}'.format(soA, soB))
formatoNum=round(soA,soB)
print('dùng hàm round:',round(soA,soB))
print('dùng hàm round:',formatoNum)

#Làm tròn số thập phân A đến B chữ số sau dấu phẩy (Có xử lý ngoại lệ đầu vào).
# cách này làm code nặng hơn vì đưa hết biến vào try
try:
    soA = float(input())
    soB = int(input())
    print('dùng hàm format:{0:.{1}f}'.format(soA, soB))
except:
    print('không hợp lệ:')

giaTriA = input() #Nhap gia tri dau tien tu ban phim
giaTriB = input() #Nhap gia tri thu hai tu ban phim

try: #Khoi lenh co the phat sinh loi
    soA = float(giaTriA) #Ep kieu giaTriA sang kieu so thuc
    soB = int(giaTriB) #Ep kieu giaTriB sang kieu so nguyen
#Dung ham format de dinh dang chuoi dau ra
    print('{0:.{1}f}'.format(so1, so2))
except: #Khoi lenh duoc thuc thi khi loi xay ra
    print("Dinh dang dau vao khong hop le!") #In thong bao