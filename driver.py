from home import HomeHandler
import tornado

application = tornado.web.Application([
(r"/", HomeHandler),
],
    cookie_secret="kdbgddsak",
    template_path="C:\\Users\\ashit\PycharmProjects\\gitProject__challengecc_socialNetwork\\frontend"
)


application.listen(8880)
tornado.ioloop.IOLoop.current().start()
