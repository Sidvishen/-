import threading
import time

class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False
class Cafe:
    def __init__(self, tables):
        self.queue = []
        self.tables = tables
        self.customer_count = 1
    def customer_arrival(self):
        while True:
            self.serve_customer(self.customer_count)
            self.customer_count += 1
            time.sleep(1)
    def serve_customer(self, customer_number):
        print(f"Посетитель {customer_number} прибыл")
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print(f"Посетитель {customer_number} сел за стол {table.number}")
                self.start_serving(customer_number, table)
                return
        self.queue.append(customer_number)
        print(f"Посетитель {customer_number} ожидает свободный стол")
    def start_serving(self, customer_number, table):
        threading.Thread(target=self.serve, args=(customer_number, table)).start()
    def serve(self, customer_number, table):
        time.sleep(5)
        table.is_busy = False
        print(f"Посетитель {customer_number} покушал и ушёл")

class Customer(threading.Thread):
    def __init__(self, cafe, customer_number):
        super().__init__()
        self.cafe = cafe
        self.customer_number = customer_number
    def run(self):
        time.sleep(5)
        print(f'Посетитель {self.number} покушал и ушёл')
        self.table.is_busy = False
        if not self.queue.empty():
            next_customer = self.queue.get()
            self.cafe.serve_customer(next_customer)

table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]
cafe = Cafe(tables)

for i in range(1):
    customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
    customer_arrival_thread.start()
    customer_arrival_thread.join()