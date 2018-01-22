class Student():
    pass
s=Student()
s.name='tom'
print(s.name)

def set_age(self,age):
    self.age=age
from types import MethodType
s.set_age=MethodType(set_age,s) #给实例绑定方法，这种方式可以调用对象内部的属性
s.set_age('xc')
print(s.age)

def fun():
    print(1)
s.fun=fun  #这种方式不能调用实例内部存在的属性、方法
s.fun()


stu2=Student()
#stu2.set_age(23) #对新建实例无效

def set_score(self,score):
    self.score=score
Student.set_score=set_score
s.set_score(100)
print(s.score)
stu2.set_score(299)
print(stu2.score)

class Animal():
    __slots__=('name','age','score')
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
am=Animal('su',12,99) #slots去掉‘score’ 会报错
print(am.name)

class Dog(Animal):
    __slots__=('name')
    
dog=Dog('x',1,1)
dog.score=99  #slots对子类无效

class Screen():
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,width):
        if isinstance(width,int):
            self._width=width
        else:
            raise ValueError('must be int ')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,height):
        self._height=height

scr=Screen()
scr.width=2
scr.height=34
print(scr.width)
print(scr.height)


