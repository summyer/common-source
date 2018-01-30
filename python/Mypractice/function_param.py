# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 20:03:11 2018

@author: Administrator
"""

def fun(name,age,*,score,**args):
    print(name,age)
    print(score)
    print(args)
    
fun('s',23,score=45,a=1,b=3,c=2)