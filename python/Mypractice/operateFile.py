#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##在保存源代码时，就需要务必指定保存为UTF-8编码。当Python解释器读取源代码时，
##为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
try:
    f=None
    f=open('./test.txt')
    print(f.read())
except IOError as e:
    print('this is no file')
finally:
    if f:
        f.close()


with open('./test.txt','r') as f:
    for line in f.readlines():
        print(line.strip())

with open('./test.txt','a') as f:
    f.write('write ...')

f1 = open('./test.jpg','rb')
a=f1.read()
##print(a.decode('ascii', errors='ignore'))

f2=open('./test.jpg','r',errors='ignore')
##print(f2.read())

a=b'124'
print(a)

## StringIO和BytesIO

from io import StringIO
f=StringIO()
f.write('hello')
print('######')
print(f.getvalue())
print(f.readline())

ts='hello\nhi\nGoodbye'
f2=StringIO(ts)
while True:
    s=f2.readline()
    if s=='':
        break
    print(s.strip())

from io import BytesIO
b=BytesIO()
b.write('hello'.encode('utf-8'))
print(b.getvalue())
b2=BytesIO(b.getvalue()) #BytesIO(b'hello')
print(b2.read().decode('utf-8'))

import os
print(os.name) #如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统

#print(os.environ.get('path'))

print(os.path.abspath('../'))
print(os.path.abspath('.'))

newfile=os.path.join(os.path.abspath('./'),'testdir')
print(newfile)
os.mkdir(newfile)
os.rmdir(newfile)

print([x for x in os.listdir('.') if os.path.isdir(x)])

#print(os.chdir('.'))


import pickle
d=dict(name='Bob',age=20,score=88)
print(pickle.dumps(d))
f=open('dump.txt','wb')
pickle.dump(d,f)
f.close()

f=open('dump.txt','rb')
d=pickle.load(f)
f.close()
print(d)


import json


class Student(object):


    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score

s=Student('Bob',20,80)
def student2dict(std):
    return {
            'name':std.name,
            'age':std.age,
            'score':std.score
        }
print(json.dumps(s,default=student2dict))

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
def dict2student(d):
    return Student(d['name'],d['age'],d['score'])
print(json.loads(json_str,object_hook=dict2student))

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)

print('a' in ['a','b'])


#set  add(key)  remove(key)
L = ['Hello', 'World', 18, 'Apple', None]
print([ele.lower() for ele in L if isinstance(ele, str)])
print([ s.lower() if isinstance(s,str) else s for s in L]) #不忽略list中的数字


s = set([1, 2, 3])
#print(s[0]) #error
