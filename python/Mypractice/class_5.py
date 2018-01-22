
from enum import Enum
Month=Enum('month',('Jan','Feb','Mar','Apr'))
for name,member in Month.__members__.items():
    #print()函数也可以接受多个字符串，用逗号“,”隔开，就可以连成一串输出：
    print(name,'=>',member,',',member.value)
from enum import unique
@unique
class Weekday(Enum):
    Sun=0
    Mon=1
    Tue=2
    Wed=3
    Thu=4
    Fri=5
    Sat=6
print(Weekday.Sun)
print(Weekday['Sun'])
print(Weekday(0))
for name,member in Weekday.__members__.items():
    print(name,'>=',member,',',member.name,member.value)


class Gender(Enum):
    Male=0
    Female=1
    
class Student(object):
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
stu=Student('s',Gender.Male)
if stu.gender == Gender.Male:
    print('测试通过')
else:
    print('测试失败')

#继承 执行父级构造方法
class Base():
    def __init__(self,score):
        self.score=score
        print('this is parent')
    def bar(self,message):
        print('%s from parent' % message)
        
class Student(Base):
    def __init__(self,name,score):
        print('**********')
        print(type(self))
        print(type(self).mro())
        super(Student,self).__init__(score) #注意super参数是Student
        print('child')
        self.name=name
    def bar(self,message):
        super(Student,self).bar(message)
        print('child bar function')
        print(self.name)
        print(self.score)
        Base.bar(self,message)  #单继承可用这种方式
    def test():
        print('s')
s=Student('s',99)
print('-----------------------')
s.bar('hello')
print(Student.mro()) # MRO
Student.test()


class A:
    def __init__(self):
        self.n = 2

    def add(self, m):
        print('self is {0} @A.add'.format(self))
        self.n += m


class B(A):
    def __init__(self):
        self.n = 3

    def add(self, m):
        print('self is {0} @B.add'.format(self))
        super().add(m)
        self.n += 3
b = B()
b.add(2)
print(b.n) # 3 + 2 +3  注意self取值

#1.super().add(m) 确实调用了父类 A 的 add 方法。
#2.super().add(m) 调用父类方法 def add(self, m) 时,
# 此时父类中 self 并不是父类的实例而是子类的实例,
# 所以 b.add(2) 之后的结果是 5 而不是 4 。

#参照  super详解
#https://mozillazg.com/2016/12/python-super-is-not-as-simple-as-you-thought.html
#后续见class_6.py  
