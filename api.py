import tornado.ioloop
import tornado.web
from customer import Customer
from addhandler import AddHandler
from delhandler import DelHandler
from gethandler import GetHandler

custs = Customer()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Customers information Microservice v1")

def make_app():
    return tornado.web.Application([
        (r"/v1", MainHandler),
        (r"/v1/addcustomer", AddHandler, dict(custs=custs)),
        (r"/v1/delcustomer", DelHandler, dict(custs=custs)),
        (r"/v1/getcustomers", GetHandler, dict(custs=custs)),
        ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


#http://localhost:8888/v1/addcustomer?name="Robert Brownie Jr."&contact="1234323409"
#http://localhost:8888/v1/addcustomer?name="Brownie Spears"&contact="7865676509"
#http://localhost:8888/v1/getcustomers
#http://yourserver:8888/v1/delcustomer?name="Robert Brownie Jr."
#http://yourserver:8888/v1/delcustomer?title="#not a customer"