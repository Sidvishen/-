class House:
    def __init__(self, numberOfFloors):
        self.numberOfFloors = numberOfFloors
        self.numberOfFloors = 5

house = House(5)

for floor in range(1, house.numberOfFloors + 1):
    print("Текущий этаж равен", floor)

