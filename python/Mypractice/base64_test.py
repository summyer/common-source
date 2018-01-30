import base64
s=b'binary\x00string'
be=base64.b64encode(s)
print(be)
print(be.decode('ascii'))
bd=base64.b64decode(be)
print(bd)


#字符转字节实际上是根据编码表去对应的如（utf-8,ascii,unicode）只不过ascii编码
#表中没有中文编码所以将中文按ASCII编码时回出现问题
chinese='我是中国人'
utf_chinese=chinese.encode('utf-8')
#unicode_chinese=chinese.encode('Unicode')
print(utf_chinese)
#print(unicode_chinese)
test='\u4E25'
print(test)

# decimal：十进制

# 普通十进制
# 0       八进制
# 0x      十六进制

#\u  unicode编码
