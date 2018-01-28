import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in'.encode('utf-8'))
md5.update('python haslib?'.encode('utf-8'))
print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('how to use md5 in'.encode('utf-8'))
sha1.update('python haslib?'.encode('utf-8'))
print(sha1.hexdigest())


import hmac

message = b'Hello,world!'
key = b'secret'
h = hmac.new(key,message,digestmod='md5')
print(h.hexdigest())

print('Hello,world!'.encode('utf-8'))
print('Hello,world!'.encode('gb2312'))


import random


def hmac_md5(key,s):
    return hmac.new(key.encode('utf-8'),s.encode('utf-8'),digestmod='md5').hexdigest()

class User(object):

    def __init__(self,name,password):
        self.name=name
        self.key=''.join([chr(random.randint(48,122)) for i in range(20)])
        self.password=hmac_md5(self.key,password)
        
db = {
    'michael':User('michael','123456'),
    'bob':User('bob','abddfa'),
    'alice':User('alice','alice203')
}
def login(username,password):
    user=db[username];
    return user.password == hmac_md5(user.key,password)

print(login('michael','123456'))
print(login('bob','hello'))



import itertools

for key, group in itertools.groupby('aaabbbccc'):

    print(type(key),type(group))

    print(key,list(group))


natuals = itertools.count(1,2)
#for n in natuals:
    #print(n)
a=sum([1,2,4])
print(a)
