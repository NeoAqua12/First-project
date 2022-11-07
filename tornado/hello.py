import tornado.ioloop
import tornado.web
import asyncio
class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, World")

def make_app():
    return tornado.web.Application([
        (r"/", HelloHandler)
    ],
    debug = True,
    autoread = True)
if __name__ == "__main__" :
    app = make_app()
    port = 8888
    print('Server is listening on localhost on port {8888}')    
    tornado.ioloop.IOLoop.current().start()
