#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Time: 2019/5/21 10:16 PM
@Author: cuberqiu
@File: websocketclient.py
@Description: 
"""

import json
from tornado.ioloop import IOLoop
from tornado import gen
from tornado.websocket import websocket_connect


@gen.coroutine
def main():
    client = yield websocket_connect('ws://127.0.0.1:8080/')
    client.write_message(json.dumps({'body': 'foo'}))

    while True:
        message = yield client.read_message()
        if message:
            print(message)



if __name__ == "__main__":
    IOLoop.current().run_sync(main)