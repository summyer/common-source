from collections import Iterable
print('***************welcome to Student Mangage System*******************')
print('***************************1.注册   2.登录*************************')
name = input('what\'t your choice:')
if name == 1:
    print('you have choiced 1')
else:
    print('you have choiced 2')
print
def doList(L):
    if isinstance(L,Iterable):
        for i in L:
            print(i)
    else:
        try:
            for i in L:
                print(i)
        except TypeError:
            print('cause error')
a = [1,3,]
doList(a)
doList(1)

