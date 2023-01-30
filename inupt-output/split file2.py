try:
	fileInp = open('inputBai12.inp', 'r',encoding='utf-8')
	data = fileInp.readlines()
	stringjoin = ' '.join(data).replace('\n','')
	danhsachcactu=stringjoin.split()
	stringjoin= ' '.join(danhsachcactu)
	fileOut = open('outputBai12.out','wb')
	fileOut.write(stringjoin.encode('utf8'))
except:
	print('có lỗi:')