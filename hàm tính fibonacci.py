
def fibonacci(n):
    if n==1 or n==2:
        return 1
    return fibonacci(n-1)+ fibonacci(n-2)

try:
    n = int(input())
    if n<=0:
        print('vui lòng nhập số nguyên dương')
    else:
        print(fibonacci(n))
except:
    print("Dinh dang dau vao khong hợp lệ")
          