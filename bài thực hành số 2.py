giatri1 = input() #Nhap gia tri thu nhat
giatri2 = input() #Nhap gia tri thu hai

try: #Khoi lenh co the phat sinh loi
   so1 = int(giatri1) #Ep kieu giatri1 sang so nguyen
   so2 = int(giatri2) #Ep kieu giatri2 sang so nguyen
   tong = so1 + so2 #Tinh tong hai so
   print("tong hai so la: ", tong) #In tong hai so
except: #Khoi lenh duoc thuc thi khi loi xay ra
   print("dinh dang dau vao khong hop le!") #In thong bao
   
   
try: print('sum=',int(input('1st:'))+int(input('2nd:'))) 
except: print('không hợp lệ')