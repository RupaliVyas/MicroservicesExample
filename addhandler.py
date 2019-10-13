import tornado.web
from customer import Customer
import json


class AddHandler(tornado.web.RequestHandler):
    def initialize(self, custs):
        self.customers = custs
        
    def get(self):
        name = self.get_argument('name')
        contact = self.get_argument('contact')
        result = self.customers.add_cust(name, contact)
        self.write(result)