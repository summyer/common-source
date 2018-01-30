class Student(object):
    def __init__(self,name):
        self.name=name

def getName(self):
    return self.name

s=Student('sxk')
s.getName=getName
#print(s.getName())  此处self不好取 使用MethodType可以绑定self
