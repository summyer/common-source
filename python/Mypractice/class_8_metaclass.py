class Field():
    def __init__(self,name,column_type):
        self.name=name
        self.column_type=column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__,self.name)
class StringField(Field):
    def __init__(self,name):
        super(StringField,self).__init__(name,'varchar(100)')

class IntegerField(Field):
    def __init__(self,name):
        super(IntegerField,self).__init__(name,'bigint')

##编写最复杂的ModelMetaclass了：
class ModelMetaclass(type):

    def __new__(cls,name,bases,attrs):
        if name == 'Mode':
            return type.__new__(cls,name,bases,attrs)
        print('Found mode: %s' % name)
        mappings=dict()
        for k , v in attrs.items():
            if isinstance(v,Field):
                print('Found mapping: %s ==> %s' % (k,v))
                mappings[k]=v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__']=mappings
        attrs['__table__']=name
        return type.__new__(cls,name,bases,attrs)

class Model(dict,metaclass=ModelMetaclass):

    def __init__(self,**kw):
        print(type(self))
        super(Model,self).__init__(**kw)

    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'model' object has no attribute %s " % key)

    def __setattr__(self,key,value):
        self[key]=value

    def save(self):
        fields=[]
        params=[]
        args=[]
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self,k,None))
        sql='insert into %s (%s) values (%s)' % (self.__table__,','.join(fields),','.join(params))
        print('sql : %s' % sql)
        print('ARGS: %s' % str(args))

##print(len(dir(Model)))
##使用model
class User(Model):
    id=IntegerField('id')
    name=StringField('username')
    email=StringField('email')
    password=StringField('password')

# 创建实例
u = User(id=1236,name='Michael',email='test@orm.org',password='my-pwd')
u.save()


##raise AttributeError(r"'model' object has no attribute %s " % 'tel')
##print(u.tel)
print(type([1,2,3]))
print(','.join(['1','2','2']))
for k,v in u.items():
    print(k)

# 1.查看注释 2.__setattr__此类方法可继承

