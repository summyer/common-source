# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 21:02:02 2018

@author: Administrator
"""
import time ,uuid

class Student():
    name='sxk'
    def __init__(self):
        pass

print(Student.name)
print(Student().name)

print ('%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex))

import orm
from models import User, Blog, Comment
import asyncio 

async def test(loop):
    await orm.create_pool(loop,user='root',password='123456',db='awesome')
    
    u = User(name='Test', email='test@1sd23.com',passwd='123456',image="about:blank")
    print(11)
    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
#
# 记得查看model中属性和表属性间的映射关系
# 解决运行出现的bug
