try:
	fileInp = open('input.inp','r',encoding='utf-8')
	ten = fileInp.readline().rstrip('\n')
	tuoiHienTai = int(fileInp.readline())
	fileOut = open('output1.out','wb') 
	Stringtosave = ('Vào 20 năm nữa, tuổi của {} sẽ là {}'.format(ten, tuoiHienTai + 20))
	fileOut.write(Stringtosave.encode('utf8'))
except FileNotFoundError:
    print('không tìm thấy fille')
except FileExistsError:
    print('file không tồn tại')
except:
	print('định dạng file không hợp lệ:')
