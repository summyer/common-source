class Student():
    def __init__(self,name="sx"):
        self.name=name
    def __getattr__(self,attr):
        if attr=='score':
            return 99
        if attr=='age':
            return lambda :19
        raise AttributeError('has no attribute %s' % attr)
    def __call__(self):
        print('my nam is %s' % self.name)
stu=Student()
print(stu.score)
print(stu.age())
#print(stu.abc)
stu()
print(callable(Student()))
print(callable(max))

class Chain():
    def __init__(self,path=""):
        self._path=path
    def __getattr__(self,attr):
        if attr == 'users':
            return lambda x:Chain('%s/%s' % (self._path,attr+'/:'+x))
        else:
            print(1)
            return Chain('%s/%s' % (self._path,attr))
    def __str__(self):
        return self._path

print(Chain().users('ss').a)


class Chain1(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain1('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain1().status.user.timeline.list)

class Chain3(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path): # __getattr__返回一个Chain类的实例，所以后面继续使用点符访问属性也是可以的，这就是链式调用的本质
        self._path = '{0}/{1}'.format(self._path,path)
        return self
        # return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path

    __call__ = __getattr__
    __repr__ = __str__


class Chain5(object):
    def __init__(self, path = ''):
        self._path = path
    def __getattr__(self, path):
        return Chain5('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path
    __call__ = __getattr__
    __repr__ = __str__

print(Chain5().users('Zhangsan').repos)

#解释一下流程
#1， Chain()的时候，执行init方法，下划线path的值是空串
#2， 点users的时候，先找有没有users方法，显然没有，那么就执行getattr方法了，ok，下划线path变为/users
#3， 这时候getattr方法返回的是Chain（）对象，后面是('Zhangsan')，相当于Chain（）('Zhangsan'),大家看下廖大大的教程，看懂了的就知道解释器去找 下划线call 方法了，call方法和getattr方法相等，于是下划线path变为/users/Zhangsan了
#4， 执行.repos没啥说的，下划线path就是/users/Zhangsan/repos

print((Chain3('/status').users)('michael').repos)



