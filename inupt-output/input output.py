#Mo file voi mode='r' de doc file
with open('input.inp', 'r') as fileInp:

#Doc 1 dong du lieu tu file va luu vao bien ten
#Su dung phuong thuc rstrip de loai bo ky tu xuong dong '\n'
    ten = fileInp.readline().rstrip('\n')

#Doc 1 dong du lieu tu file va luu vao bien tuoiHienTai
    tuoiHienTai = int(fileInp.readline())

#Mo file voi mode='w' de ghi file
with open('output.out', 'w') as fileOut:
#Ghi noi dung vao file theo mau
    fileOut.write('Vao 20 nam nua, tuoi cua {} se la {}'.format(ten, tuoiHienTai + 20))

fileInp = open('input.inp','r') 
ten = fileInp.readline().rstrip('\n')
tuoiHienTai = int(fileInp.readline())
fileOut = open('output1.out','w') 
fileOut.write('Vao 20 nam nua, tuoi cua {} se la {}'.format(ten, tuoiHienTai + 20))
