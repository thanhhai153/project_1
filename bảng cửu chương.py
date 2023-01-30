try:
    a = int(input())
    if a in range(1,9):
        for n in range(1,10):
            print('{} x {} = {}'.format(a,n,a*n))
    else:
        print('Chi tinh duoc bang cuu chuong 1 den 9 thoi!')
except:
    print('định dạng đầu vào không hợp lệ')        