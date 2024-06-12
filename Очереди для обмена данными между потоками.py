import threading
import time
class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False
class Customer(threading.Thread):
    def __init__(self, number, table):
        super(Customer, self).__init__()
        self.number = number
        self.table = table

    def run(self):
        print(f"Посетитель {self.number} сел за стол {self.table.number}")
        time.sleep(2)
        self.table.is_busy = False
        print(f"Посетитель {self.number} покушал и ушёл")
class Cafe:
    def __init__(self, tables):
        self.tables = tables
        self.queue = []
    def customer_arrival(self, customer_number):
        print(f"Посетитель {customer_number} прибыл")
        for table in self.tables:
            if not table.is_busy:
                customer = Customer(customer_number ,table)
                table.is_busy = True
                customer.start()
                return
        self.queue.append(customer_number)
        print(f"Посетитель {customer_number} ожидает свободный стол")
    def serve_customer(self):
        while True:
            time.sleep(1)
            if self.queue:
                customer_number = self.queue.pop(0)
                for table in self.tables:
                    if not table.is_busy:
                        customer = Customer(customer_number, table)
                        table.is_busy = True
                        customer.start()
                        return

table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]
cafe = Cafe(tables)

for i in range(1, 20):
    cafe.customer_arrival(i)
cafe.serve_customer()