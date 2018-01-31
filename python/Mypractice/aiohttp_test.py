# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 20:20:32 2018

@author: Administrator
"""

import asyncio

from aiohttp import web

async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    print(text)
    return web.Response(body=text.encode('utf-8'))


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8081)
    print('Server started at http://127.0.0.1:8081...')
    return srv

loop = asyncio.get_event_loop()
#loop = asyncio.new_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

#注意aiohttp的版本  切换到2.3.9版本会出现参数错误
#chrome firefox下弹出下载
#ie 下显示页面
