class Customer:
    def __init__(self,customer_id,customer_name):
        self.customer_id = customer_id
        self.customer_name = customer_name


class BankAccount:
    def __init__(self,account_no,customer):
        self.account_no = account_no
        self.customer = customer
        self.balance = 0


class Bank:
    def __init__(self):
        self.customers=[]
        self.accounts=[]

    def create_customer(self,customer_id, customer_name):
        customer = Customer(customer_id,customer_name)
        self.customers.append(customer)
        print("CUSTOMER CREATED SUCCESSFULLY")

    def create_account(self,customer_id, account_no):
        pass

    def find_customer(self,customer_id):
        for customer in self.customers:
             if customer.customer_id==customer_id:
                 return customer
        return None
                 

        

    def find_account(self,account_no):
        pass