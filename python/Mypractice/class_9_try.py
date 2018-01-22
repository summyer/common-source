try:
    print('try')
    r=10/0
except ZeroDivisionError as e:
    print('excep:',e)
else:
    print('there is no error')
finally:
    print('finally..')
print('END')



##def foo(s):
##    return 10 / int(s)
##
##def bar(s):
##    return foo(s) * 2
##
##def main():
##    try:
##        bar('0')
##    except Exception as e:
##        print('Error:', e)
##    finally:
##        print('finally...')
##main()


def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    bar('0')

#main()


#print(__name__)

import logging
logging.basicConfig(level=logging.INFO) #需要紧接着logging，不然后面在设置不生效
try:
    a=10/0
except ZeroDivisionError as e:
    logging.exception(e)

print('继续执行。。。。。')


##class FooError(ValueError):
##    pass
##
##
##def foo(s):
##    n = int(s)
##    if n==0:
##        raise FooError('invalid value: %s' % s)
##    return 10/n
##
##foo('0')


def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise    # raise语句如果不带参数，就会把当前错误原样抛出

#bar()
print('继续执行。。。。2')


#调试
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')
#main()
##启动Python解释器时可以用-O参数来关闭assert：
##关闭后，你可以把所有的assert语句当成pass来看


##logging



s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)


#pdb
#python -m pdb err.py

