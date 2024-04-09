class Car:
    price = 1000000

    def horse_powers(self):
        price = self.price
        print("Horse powers is: ", price)
        return 100 * self.price


class Nissan(Car):
    price = 1000000

    def horse_powers(self):
        price = self.price
        print("Nissan powers is: ", price)
        return 200 * self.price



class Kia(Car):
    price = 1000000

    def horse_powers(self):
        price = self.price
        print("Kia powers is: ", price)
        return 300 * self.price


car1 = Car()
print(car1.horse_powers())
nissan1 = Nissan()
print(nissan1.horse_powers())
kia1 = Kia()
print(kia1.horse_powers())
