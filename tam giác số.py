from re import L

try:
    a = int(input())
    if a>9 and a<1:
        print("vui lòng nhập số trong khoảng từ 1 đến 9")
    else:
        for x in range(1,a+1):
            line = ""
            for i in range(1,x+1):
                line = "{} {}".format(line,i)
            print(line)
except: 
   print("Dinh dang dau vao khong hop le!")

#Khoi lenh co the phat sinh loi
try:
   #Nhap gia tri tu ban phim
   #Ep kieu du lieu sang so nguyen
   n = int(input())
  
   #Su dung cau truc re nhanh xu ly truong hop n nam ngoai (1:9)
   if n<1 or n>9:
       print("Vui long nhap gia tri tu 1 den 9!")
   else:   
       #Su dung vong 2 vong for long nhau de thuc hien yeu cau bai toan
       for hang in range(1, n+1):
           for cot in range(1, hang+1):
               #Tham so end=' ' de cac so trong hang cach nhau 1 khoang trong
               print(cot, end=' ')
           #Xong 1 hang thi xuong dong
           print()
#Khoi lenh duoc thuc thi khi loi xay ra
except:
   print("Dinh dang dau vao khong hop le!")          
   
try:
    a = int(input())
    if a>9 and a<1:
        print("vui lòng nhập số trong khoảng từ 1 đến 9")
    else:
        for x in range(1,a+1):
            line = ""
            for i in range(1,x+1):
                line = "{} {}".format(line,i)
            print(line)
except:
   print("Dinh dang dau vao khong hop le!")

#Khoi lenh co the phat sinh loi
try:
   #Nhap gia tri tu ban phim
   #Ep kieu du lieu sang so nguyen
   n = int(input())
  
   #Su dung cau truc re nhanh xu ly truong hop n nam ngoai (1:9)
   if n<1 or n>9:
       print("Vui long nhap gia tri tu 1 den 9!")
   else:   
       #Su dung vong 2 vong for long nhau de thuc hien yeu cau bai toan
       for hang in range(n):
           for cot in range(n - hang, 0, -1):
               #Tham so end=' ' de cac so trong hang cach nhau 1 khoang trong
               print(cot, end=' ')
           #Xong 1 hang thi xuong dong
           print()
#Khoi lenh duoc thuc thi khi loi xay ra
except:
   print("Dinh dang dau vao khong hop le!")
            