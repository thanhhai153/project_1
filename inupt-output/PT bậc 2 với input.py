#Import thu vien math de su dung ham sqrt tinh can bac 2
import math

#Khoi lenh co the phat sinh loi
try:
    #Mo file voi mode='r' de doc file
    fileInp = open('Bai2.10.inp', 'r')
       #Doc dong du lieu dau tien tu file
       #Su dung phuong thuc strip de loai bo ky tu xuong dong hay khoang trang
    dongDauTien = fileInp.readline().strip()
      
       #Truong hop 1: Giai phuong trinh bac nhat
    if dongDauTien == '1':
        #Doc dong du lieu thu hai tu file
        dongThuHai = fileInp.readline()
        a, b = map(float, dongThuHai.split())

        #Thuat toan giai phuong trinh bac nhat
        if a == 0:
            if b == 0:
                thongBao = "Phuong trinh co vo so nghiem"
            else:
                thongBao = "Phuong trinh vo nghiem"
        else:
            thongBao = "Phuong trinh co mot nghiem duy nhat: \nx = {}".format(-b / a)

    #Truong hop 2: Giai phuong trinh bac hai
    elif dongDauTien == '2':
        #Doc dong du lieu thu hai tu file
        dongThuHai = fileInp.readline()
        a, b, c = map(float, dongThuHai.split())
        
        #Thuat toan giai phuong trinh bac hai
        if a == 0:
            if b == 0:
                if c == 0:
                    thongBao = "Phuong trinh co vo so nghiem"
                else:
                    thongBao = "Phuong trinh vo nghiem"
            else:
                thongBao = "Phuong trinh co mot nghiem duy nhat: \nx = {}".format(-c / b)
        else:
            #Tinh delta
            delta = b * b - 4 * a * c
            #Kiem tra cac truong hop cua delta
            if delta > 0:
                x1 = float((-b + math.sqrt(delta)) / (2 * a))
                x2 = float((-b - math.sqrt(delta)) / (2 * a))
                thongBao = "Phuong trinh co hai nghiem phan biet la: \nx1 = {} \nx2 = {}".format(x1, x2)
            elif delta == 0:
                x = -b / (2 * a)
                thongBao = "Phuong trinh co nghiem kep: \nx1 = x2 = {}".format(x)
            else:
                thongBao = "Phuong trinh vo nghiem"

    #Truong hop khong chon dung chuc nang
    else:
        thongBao = "Vui long chon mot trong hai chuc nang:\n1. Giai phuong trinh bac nhat\n2.Giai phuong trinh bac hai"

#Khoi lenh duoc thuc thi khi xay ra loi "Khong tim thay file input"
except FileNotFoundError:
   thongBao = "Khong tim thay file input!"

#Khoi lenh duoc thuc thi khi xay ra loi "Sai dinh dang dau vao"
except:
   thongBao = "Dinh dang dau vao khong hop le!"

#Mo file voi mode='w' de ghi file
fileOut =  open('Bai2.10.out', 'w')
#Xuat thong bao ra file out
fileOut.write(thongBao)