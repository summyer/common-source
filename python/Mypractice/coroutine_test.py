# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 21:14:17 2018

@author: Administrator
"""
print('aa',2,3)

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = "".join(["200 OK",str(n*n)])

def produce(c):
    c.send(None)
    n = 0
    while n<5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)