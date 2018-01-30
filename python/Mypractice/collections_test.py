from collections import namedtuple

# namedtuple
Point=namedtuple('Point',['x','y'])
p=Point(1,2)
print('x:%s,%s' % (p.x,p.y))
print(isinstance(p,tuple))

# deque
from collections import deque

q=deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)
q.pop()
q.popleft()
print(q)

# defaultdict
from collections import defaultdict

dd = defaultdict(lambda:'N/A')
dd['k1']='abc'
print(dd['k1'])
print(dd['k2'])

# OrderedDict
from collections import OrderedDict
d=dict({'a':1,'b':2,'c':3})
print(d)
d2=dict([('a',1),('b',2),('c',3)])
print(d2)

od=OrderedDict({'a':1,'b':2,'c':3})
od2=OrderedDict([('a',1),('b',2),('c',3)])
print(od)
print(od2)

od3=OrderedDict()
od3['x']=1
od3['y']=2
od3['z']=3
print(od3.keys())
print(od3.values())


class LastUpdatedOrderedDict(OrderedDict):


    def __init__(self, capacity):
        super(LastUpdatedOrderedDict,self).__init__()
        self._capacity = capacity

    def __setitem__(self,key,value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:',last)
        if containsKey:
            del self[key]
            print('set:',(key,value))
        else:
            print('add:',(key,value))
        OrderedDict.__setitem__(self,key,value)

oDict=LastUpdatedOrderedDict(5)
oDict['a']=1
oDict['b']=2
oDict['c']=3
oDict['d']=4
oDict['e']=5
oDict['b']=6
print(oDict)


# Counter 是一个简单的计数器
from collections import Counter
c=Counter()
for ch in 'programminghello':
    c[ch]=c[ch]+1
print(c)

c2=Counter('hello')
print(c2)
