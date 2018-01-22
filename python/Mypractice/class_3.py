class Animal():
    pass
class Mammal(Animal):
    pass
class Bird(Animal):
    pass

class Runable():
    pass
class Flyable():
    pass

class Dog(Animal,Runable):
    pass
class Bat(Animal,Flyable):
    pass

#MixIn
s='abc'
print(len(s))
print(s.__len__())

class Student():
    def __init__(self,name):
        self.name=name
    def __str__(self): #特殊
        return 'Student object (name: %s)' % self.name
    __repr__=__str__
print(Student('name'))
Student('xd')

class Fun():
    a=0
    def set_list(self,list):
        self._list=list
    def get_list(self):
        return self._list
    def __iter__(self):
        #return iter(self._list)  # Iterable  | Iterator iter(list)
        return self
    def __next__(self):
        if self.a<len(self._list):
            b=self._list[Fun.a]
            Fun.a=Fun.a+1
            return b
        else:
            raise StopIteration()
    def __getitem__(self,n):
        return self._list[n]
    def __delitem__(self,n):
        del self._list[n]
f=Fun()
f.set_list(list(range(12)))
#print(f.get_list());
for i in f:
    print(i)
for i in f.get_list():
    print(i)
del f[0]
print(f[0])


        
