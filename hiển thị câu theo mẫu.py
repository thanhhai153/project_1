
def xin_chao(ten, tuoi):
   print("Xin chao! Toi la {}, toi {} tuoi.".format(ten, tuoi))

#Khoi lenh co the phat sinh loi
try:
   #Nhap hai gia tri tu ban phim
   #Ep kieu du lieu sang so nguyen
   ten = input()
   tuoi = int(input())
  
   #Su dung cau truc re nhanh xu ly truong hop tuoi am
   if tuoi < 1:
       print("Vui long nhap tuoi la so nguyen duong!")
   else:   
       #Goi thuc thi ham
       xin_chao(ten, tuoi)
#Khoi lenh duoc thuc thi khi loi xay ra
except:
   print("Dinh dang dau vao khong hop le!")

#Dinh nghia ham
def ten_ban_cao_hon(tenBanThuNhat, chieuCaoBanThuNhat, tenBanThuHai, chieuCaoBanThuHai):
   #So sanh chieu cao cua hai ban
   if chieuCaoBanThuNhat > chieuCaoBanThuHai:
       #Tra ve ten cua ban thu nhat
       return tenBanThuNhat
   #Tra ve ten cua ban thu hai
   return tenBanThuHai

#Khoi lenh co the phat sinh loi
try:
   #Nhap cac gia tri tu ban phim
   tenBanThuNhat, chieuCaoBanThuNhat = input().split()
   tenBanThuHai, chieuCaoBanThuHai = input().split()
   #Ep kieu du lieu chieu cao sang so nguyen
   chieuCaoBanThuNhat = int(chieuCaoBanThuNhat)
   chieuCaoBanThuHai = int(chieuCaoBanThuHai)
  
   #Su dung cau truc re nhanh xu ly truong hop chieu cao nho hon 1 va chieu cao bang nhau
   if chieuCaoBanThuNhat < 1 or chieuCaoBanThuHai < 1:
       print("Chieu cao phai lon hon 0!")
   elif chieuCaoBanThuNhat == chieuCaoBanThuHai:
       print("{} cao bang {}".format(tenBanThuNhat, tenBanThuHai))
   else:   
       #Goi thuc thi ham va truyen cac tham so cho ham
       tenBanCaoHon = ten_ban_cao_hon(tenBanThuNhat, chieuCaoBanThuNhat, tenBanThuHai, chieuCaoBanThuHai)
       print("{} cao hon.".format(tenBanCaoHon))
#Khoi lenh duoc thuc thi khi loi xay ra
except:
   print("Dinh dang dau vao khong hop le!")