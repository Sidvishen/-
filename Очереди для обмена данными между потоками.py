import queue
import threading
import time

class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False
class Cafe:
    def __init__(self, tables):
        self.tables = tables
        self.queue = queue.Queue()
        self.customers_threads = []


    def customer_arrival(self):
        for i in range(1, 21):
            print(f'Посетитель номер {i} прибыл')
            self.serve_customer(i)
            time.sleep(1)


    def serve_customer(self, customer):
        free_table = False
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print(f'Посетитель номер {customer} сел за стол {table.number}.')
                customer_thr = Customer(customer, self, self.queue, table)
                customer_thr.start()
                self.customers_threads.append(customer_thr)
                free_table = True
                return
        if not free_table:
            print(f'Посетитель номер {customer} ждёт стол.')
            self.queue.put(customer)
class Customer(threading.Thread):
    def __init__(self, number, cafe, queue, table):
        super().__init__()
        self.cafe = cafe
        self.number = number
        self.queue = queue
        self.table = table


    def run(self):
        time.sleep(5)
        print(f'Посетитель номер {self.number} покушал и ушёл')
        self.table.is_busy = False
        if not self.queue.empty():
            next_customer = self.queue.get()
            self.cafe.serve_customer(next_customer)




tables = []
for i in range(1, 4):
    tables.append(Table(i))


cafe = Cafe(tables)

th1 = threading.Thread(target=cafe.customer_arrival)
th1.start()
th1.join()

for i in cafe.customers_threads:
    i.join()





