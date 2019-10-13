import json


class Customer:

    def __init__(self):
        self.customers = []

    def add_cust(self, name, contact):
        new_cust = {}
        new_cust["Name"] = name
        new_cust["Contact"] = contact
        self.customers.append(new_cust)
        print("Customer: {0}".format(new_cust))
        return json.dumps(new_cust)

    def del_cust(self, name):
        found = False
        for idx, cust in enumerate(self.customers):
            if cust["Name"] == name:
                index = idx
                found = True
                del self.customers[idx]
        print("customers: {0}".format(json.dumps(self.customers)))
        return found

    def get_all_customers(self):
        return self.customers

    def json_list(self):
        return json.dumps(self.customers)

    def get_details(self, contact):
        found = False
        for idx, cust in enumerate(self.customers):
            if cust["Contact"] == contact:
                index = idx
                found = True
                
        print("customers: {0}".format(json.dumps(self.customers)))
        return found

    def get_val(self, contact):
        
        for idx, cust in enumerate(self.customers):
            if cust["Contact"] == contact:
                index = idx
                
        return json.dumps(self.customers[index])