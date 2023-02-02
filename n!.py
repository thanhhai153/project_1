#Khoi lenh co the phat sinh loi
try:
    #Nhap gia tri tu ban phim
    #Ep kieu du lieu sang so nguyen
    n = int(input())
    
    #Su dung cau truc re nhanh xu ly truong hop n < 0
    if n<0:
        print("Vui long nhap so tu nhien!")
    else:
        ketQua = 1
        #Su dung vong lap for duyet cac so tu 1 toi n
        for i in range(1, n+1):
            ketQua *= i 
        print(ketQua)
        
#Khoi lenh duoc thuc thi khi loi xay ra
except:
    print("Dinh dang dau vao khong hop le!")
    
    
#Khoi lenh co the phat sinh loi
try:
    #Nhap gia tri tu ban phim
    #Ep kieu du lieu sang so nguyen
    x = float(input())
    n = int(input())
   
    #Su dung cau truc re nhanh xu ly truong hop n < 0
    if n<0:
        print("Vui long nhap n la so tu nhien!")
    elif n == 0:
        print(1)
    else:
        ketQua = 1
        giaiThua = 1
        #Su dung vong lap for duyet cac so tu 1 toi n
        for i in range(1, 2*n+1):
            giaiThua *= i
            if i % 2 == 0:
                ketQua += pow(x, i)/giaiThua
            else:
                ketQua -= pow(x, i)/giaiThua 
        print('{:.5f}'.format(ketQua))
        
#Khoi lenh duoc thuc thi khi loi xay ra
except:
    print("Dinh dang dau vao khong hop le!")
    #Khoi lenh co the phat sinh loi
try:
    #Nhap gia tri tu ban phim
    #Ep kieu du lieu sang so nguyen
    n = int(input())
    
    #Su dung cau truc re nhanh xu ly truong hop n < 0
    if n < 0:
        print("Vui long nhap so tu nhien!")
    else:
        soDaoNguoc = 0
        #Su dung vong while de tach cac chu so
        while n > 0:
            chuSoCuoi = n % 10
            soDaoNguoc = soDaoNguoc * 10 + chuSoCuoi
            n = n // 10
        print(soDaoNguoc)
        
#Khoi lenh duoc thuc thi khi loi xay ra
except:
    print("Dinh dang dau vao khong hop le!") 
# chỉnh sửa ngyaf 2/2
