import multiprocessing


class WarehouseManager:
    def __init__(self):
        self.data = {}

    def process_request(self, request):
        action, product, quantity = request
        if action == 'receipt':
            if product in self.data:
                self.data[product] += quantity
            else:
                self.data[product] = quantity
        elif action == 'shipment':
            if product in self.data and self.data[product] >= quantity:
                self.data[product] -= quantity

    def run(self, requests):
        requests = [
            ("product1", "receipt", 100),
            ("product2", "receipt", 150),
            ("product1", "shipment", 30),
            ("product3", "receipt", 200),
            ("product2", "shipment", 50)
        ]
        for request in requests:
            process = multiprocessing.Process(target=self.process_request, args=(request,))
            # processes.append(process)
            process.start()

        for request in requests:
            print(requests)
            print(self.data)
            print(self.data[request])


if __name__ == '__main__':
    warehouse_manager = WarehouseManager()
    requests = [('receipt', 'apple', 10), ('receipt', 'banana', 5), ('shipment', 'apple', 3)]
    warehouse_manager.run(requests)
    print(warehouse_manager.data)