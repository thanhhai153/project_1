#Nhập & tính tổng dãy số nguyên bất kỳ cách nhau bởi khoảng trắng.
#sum string
#Nhap dong du lieu chua day gia tri tu ban phim
print('nhập dãy số với khoảng trắng:')
dayGiaTri = input()

#Su dung ham split() de cat day gia tri thanh cac chuoi con
danhSachGiaTri = dayGiaTri.split()
try:
#Su dung ham map() de thuc hien viec chuyen cac chuoi con sang kieu so nguyen
    danhSachSo = map(int, danhSachGiaTri)

#Su dung ham sum() de tinh tong day so
    tongDaySo = sum(danhSachSo)

#In ket qua ra man hinh
    print('tổng dãy số trên:',tongDaySo)

except:
    print('không hợp lệ:')