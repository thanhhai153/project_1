import math
from re import A

#Khoi lenh co the phat sinh loi
try:
   #Nhap gia tri tu ban phim
   #Ep kieu du lieu sang so nguyen
   n = int(input())
  
   #Su dung cau truc re nhanh xu ly truong hop n <= 0
   if n < 0:
       print("Vui long nhap so tu nhien!")
   elif n < 2:
       print("{} khong la so nguyen to!".format(n))
   else:
       #Su dung vong lap for de duyet cac so tu 2 den can bac hai cua n
       for i in range(2, int(math.sqrt(n))+1):
           #Kiem tra tinh chia het
           if n % i == 0:
               print("{} khong la so nguyen to!".format(n))
               #Thoat vong lap
               break
       #Neu khong thoat vong lap thi khoi lenh else se duoc thuc hien
       else:
           print("{} la so nguyen to!".format(n))
#Khoi lenh duoc thuc thi khi loi xay ra
except:
   print("Dinh dang dau vao khong hop le!")
   
   
   
import math

#Khoi lenh co the phat sinh loi
try:
   #Nhap hai so tu ban phim
   #Ep kieu du lieu sang so nguyen
   a = int(input())
   b = int(input())
  
   #Su dung cau truc re nhanh xu ly cac truong hop
   if a < 0 or b < 0:
       print("Vui long nhap so tu nhien!")
   elif a > b:
       print("So thu nhat lon hon so thu hai!")
   else:
       #Su dung vong lap for duyet cac so tu a den b
       for i in range(a, b + 1):
           if i > 1:       
               #Su dung vong lap for de duyet cac so tu 2 den can bac hai cua i
               for j in range(2, int(math.sqrt(i))+1):
                   #Kiem tra tinh chia het
                   if i % j == 0:
                       #Thoat vong lap
                       break
               #Neu khong thoat vong lap thi khoi lenh else se duoc thuc hien
               else:
                   print(i, end=' ')
#Khoi lenh duoc thuc thi khi loi xay ra
except:
   print("Dinh dang dau vao khong hop le!")