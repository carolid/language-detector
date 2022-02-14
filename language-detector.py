from langdetect import detect
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop


class HelloHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type", 'application/json')

    def get(self):
        self.write({'message': 'hello world'})

    def post(self):
        value = self.get_argument('Raw')
        langDetect = detect(value)
        self.write(langDetect)


def make_app():
    urls = [("/", HelloHandler)]
    return Application(urls)


if __name__ == '__main__':
    app = make_app()
    app.listen(3000)
    IOLoop.instance().start()

