import asyncio
import os
import time
from aiohttp import web


def index(request):
    """
    首页
    """
    return web.Response(body=b'<h1>Hello</h1>', content_type='text/html')


async def main(loop):
    app = web.Application(loop=loop)
    app.router.add_route("GET", "/", index)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    return srv
    
loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.run_forever()
