def giai_thua(n):
    if n == 0:
        return 1
    return n * giai_thua(n-1)
try:    
    n = int(input())
    if n < 0:
        print("Vui long nhap so tu nhien!")
    else:
        print(giai_thua(n))
except:
    print('đầu vào không hợp lệ')