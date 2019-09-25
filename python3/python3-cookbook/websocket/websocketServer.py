from tornado import websocket, web, ioloop, gen

class MainHandler(websocket.WebSocketHandler):
    def open(self, *args, **kwargs):
        print("the websocket is opened")
        print(self.settings["settings"])
        self.write_message("opened")

    @gen.coroutine
    def on_message(self, message):
        print("get message: "+message)
        print("messae type : {}".format(type(message)))
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("WebSocket closed")
        self.write_message("WebSocket closed")

    def check_origin(self, origin):
        return True


handlers = [
    (r'/', MainHandler),
]

if __name__=="__main__":
    app = web.Application(handlers, debug=True)
    app.settings["settings"]="my set"
    app.listen(8080)
    ioloop.IOLoop.instance().start()