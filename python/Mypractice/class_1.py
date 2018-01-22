class Animal():
    def __init__(self):
        self.name='Animal'
    def run(self):
        print('%s is running' % self.name)

class Dog(Animal):
    def __init__(self):
        self.name='Dog'
    def run(self):
        print('%s is running' % self.name)

class Cat(Animal):
    def __init__(self):
        self.name='Cat'
    def run(self):
        print('%s is running' % self.name)
animal=Animal()
animal.run()
dog=Dog()
cat=Cat()
dog.run()
cat.run()
a=list()
b=Animal()
c=Dog()
print(isinstance(a,list))
print(isinstance(b,Animal))
print(isinstance(c,Dog))

def run_twice(animal):
    animal.run()
    animal.run()
run_twice(Dog())
run_twice(Cat())

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running')
run_twice(Tortoise())
def test_run():
    print('this is a test')
a={'run':test_run}
print(a['run'])
class Timer():
    def run(self):
        print('start...')
run_twice(Timer())
#print(dir(()))
class Student():
    love='sxk'
    def __init__(self,name,age):
        self.__name=name
        self.age=age
stu=Student('xc',12)
#print(dir(stu))
print(hasattr(stu,'name'))
print(hasattr(stu,'age'))
print(getattr(stu,'age'))
#print(getattr(stu,'name'))
print(stu.love)
stu.love='aa'
print(stu.love)
print(Student.love)
del stu.love
print(stu.love)

