from scrapy import cmdline
from data import init_database, open_database
from tornado.web import Application
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from api import PerMinuteSpeedHandler


def make_apiapp():
    return Application([
        (r"/speedperminute", PerMinuteSpeedHandler)
    ])


if __name__ == '__main__':
    app = make_apiapp()
    server = HTTPServer(app)
    server.listen(8080)
    open_database()
    init_database()
    name = 'UserCrawler'
    cmdline.execute(('scrapy crawl ' + name).split())
    try:
        IOLoop.current().start()
    except KeyboardInterrupt:
        pass
