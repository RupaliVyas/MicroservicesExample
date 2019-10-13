
import tornado.web
from customer import Customer
import json


class GetDetails(tornado.web.RequestHandler):
	def initialize(self, custs):
		self.customers = custs
	def getdet(self,contact):
		contact = self.get_argument('contact')
		result = self.customers.get_details(contact)
		if result:
			self.write(self.customers.get_val(contact))
			self.set_status(200)
		else:
			self.write("Customer '{0}' not found".format(contact))
			self.set_status(404)
