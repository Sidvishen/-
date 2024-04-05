class Buiding:
    def __init__(self, numberOfFloors=None, buildingType=None):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType


    def __eq__(self, other):
        return (self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType)

buiding = Buiding(1, 'Крипичный')
buiding1 = Buiding(1, 'Крипичный')
buiding2 = Buiding(2, 'Деревянный')


print(buiding == buiding1)
print(buiding == buiding2)








