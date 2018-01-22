def normalize(a):
    return a.capitalize()
L1=['adam','LISA','barT']
L2=list(map(normalize,L1))
print(L2)
print(map(normalize,L1))
from functools import reduce
L3=[1,2,3,4,5,6]
def pord(L):
    return reduce(lambda x,y:x*y,iter(L))
print(pord(L3))
print(0.1**3)

i=0
c=False
def str2float(v):
    a={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    l=iter(v)
    #print(list(l))  #如果不注释掉这行代码，执行完后迭代器就空了，后面的reduce就出错，l为空
    def pa(x,y):
        global i
        global c
        print('i=',i,'c=',c)
        
        if y != '.' and not c:
            if isinstance(x,str):
                x=a[x]
            if isinstance(y,str):
                y=a[y]
            return x*10+y
        elif y == '.':
            c=True
            if isinstance(x,str):
                x=a[x]
            return x
        else:
            i+=1
            if isinstance(y,str):
                y=a[y]
            return x + 0.1**i*y
    #reduce(pa,map(lambda x:x,v))
    print(reduce(pa,l))
f_1='244.135'
str2float(f_1)

print(9.3/2.0)
print(9.3//2.0)
print(9.3%2.0)
print(9%2)

