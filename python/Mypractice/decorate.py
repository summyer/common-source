def show(a):
    print('this is a test %s' % a)
def log(fn):
    def wapper(*a,**b):
        print('this is log')
        fn(*a,**b)
    return wapper

show=log(show)
show(1)
    
