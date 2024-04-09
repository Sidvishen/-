class Vehicle:
    vehicle_type = "none"

class Car:
    price = 1000000

    def horse_powers(self):
        self.price
        print(self.price)
        print("Nissan powers is: ")
        return 200 * self.price

class Nissan(Vehicle, Car):
    def horse_powers(self):
        return 200 * self.price

vehicle = Vehicle()
vehicle.vehicle_type = "none"
print(vehicle.vehicle_type)
car = Car()
car.horse_powers()
print(car.horse_powers())


