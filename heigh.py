#Nhap ten va chieu cao cua ban thu nhat
print('nhập tên và chiều cao bạn 1:')
tenBan1, chieuCaoBan1 = input().split()
print('nhập tên và chiều cao bạn 2 :')
#Nhap ten va chieu cao cua ban thu hai
tenBan2, chieuCaoBan2 = input().split()

#Khoi lenh co the phat sinh loi
try:
   #Ep kieu sang so nguyen
   chieuCaoBan1 = int(chieuCaoBan1)
   chieuCaoBan2 = int(chieuCaoBan2)

   #Xu ly truong hop du lieu chieu cao am
   if chieuCaoBan1 <= 0 or chieuCaoBan2 <= 0:
       print('Chieu cao phai lon hon 0!')
   #Xu ly truong hop chieu cao bang nhau
   elif chieuCaoBan1 == chieuCaoBan2:
       print(tenBan1 + " cao bang " + tenBan2)
   #So sanh chieu cao va xuat thong bao
   elif chieuCaoBan1 > chieuCaoBan2:
       print(tenBan1 + " cao hon " + tenBan2)
   else:
       print(tenBan2 + " cao hon " + tenBan1)

#Khoi lenh duoc thuc thi khi loi xay ra
except:
  print("dinh dang dau vao khong hop le!") #In thong bao
  
#test
#test branch