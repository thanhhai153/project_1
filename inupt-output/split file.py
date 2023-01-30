#Mo file voi mode='r' de doc file
fileInp = open('inputBai12.inp', 'r',encoding='utf-8')

#Dung ham read() doc toan bo du lieu tu file
toanBoFile = fileInp.read()

#Dung ham splitlines() cat du lieu theo tung dong va luu thanh danh sach
danhSachCacDong = toanBoFile.splitlines()

#Dung ham join() noi cac dong du lieu lai cach nhau 1 khoang trang
cauChaoHoanChinh = ' '.join(danhSachCacDong)

#Mo file voi mode='w' de ghi file
fileOut = open('Bai1.12.out', 'w')

#Ghi noi dung vao file
fileOut.write(cauChaoHoanChinh)