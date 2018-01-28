import chardet

data = '离离原上草'.encode('gbk')

charset=chardet.detect(data)
print(charset)
