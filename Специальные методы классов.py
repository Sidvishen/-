class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(f"number of floors set to: {self.numberOfFloors}")

myHouse = House()
myHouse.setNewNumberOfFloors(2)
