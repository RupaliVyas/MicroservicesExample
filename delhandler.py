
import tornado.web
from customer import Customer
import json


class DelHandler(tornado.web.RequestHandler):
    def initialize(self, custs):
        self.customers = custs
        
    def get(self):
        name = self.get_argument('name')
        result = self.customers.del_cust(name)
        if result:
            self.write("Deleted Customer Name : {0} successfully".format(name))
            self.set_status(200)
        else:
            self.write("Customer '{0}' not found".format(name))
            self.set_status(404)