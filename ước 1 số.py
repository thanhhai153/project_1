#Khoi lenh co the phat sinh loi
try:
   #Nhap gia tri tu ban phim
   #Ep kieu du lieu sang so nguyen
   n = int(input())
  
   #Su dung cau truc re nhanh xu ly truong hop n < 0
   if n < 0:
       print("Vui long nhap so tu nhien!")
   else:
       #Su dung vong lap for de duyet cac so tu 1 den n
       for i in range(1, n+1):
           #Kiem tra tinh chia het
           if n % i == 0:
               print(i, end=' ')
      
#Khoi lenh duoc thuc thi khi loi xay ra
except:
   print("Dinh dang dau vao khong hop le!")
   
   
# số hoàn thiện
#Khoi lenh co the phat sinh loi
try:
   #Nhap gia tri tu ban phim
   #Ep kieu du lieu sang so nguyen
   n = int(input())
  
   #Su dung cau truc re nhanh xu ly truong hop n <= 0
   if n <= 0:
       print("Vui long nhap so nguyen duong!")
   else:
       tongCacUoc = 0
       #Su dung vong lap for de duyet cac so tu 1 den n // 2 + 1
       for i in range(1, n // 2 + 1):
           #Kiem tra tinh chia het
           if n % i == 0:
               #Tinh tong cac uoc
               tongCacUoc += i
       if n == tongCacUoc:
           print("{} la so hoan thien!".format(n))
       else:
           print("{} khong la so hoan thien!".format(n))
#Khoi lenh duoc thuc thi khi loi xay ra
except:
   print("Dinh dang dau vao khong hop le!")