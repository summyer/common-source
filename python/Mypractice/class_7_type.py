from hello import Hello as tHello
h=tHello()
h.hello()
print(type(tHello))
print(type(h))


#type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，
#我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：
def fn(self,name='world'):
    print('hello , %s' % name)
Hello=type("Hello",(),dict(hello=fn))
h2=Hello()
h2.hello()
print(Hello.mro())


#元类
## metaclass是类的模板，所以必须从`type`类型派生
class ListMetaclass(type):
    def __new__(cls,name,bases,attrs):
        print('############')
        print(cls)
        print(name)
        print(bases)
        print(type(attrs))
        attrs['add']=lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)
class MyList(list,metaclass=ListMetaclass):
    pass
L=MyList()
L.add(1)
print(L)
#print(dir(L))
#print(dir(MyList))
#动态修改有什么意义？直接在MyList定义中写上add()方法不是更简单吗？
#正常情况下，确实应该直接写，通过metaclass修改纯属变态。
