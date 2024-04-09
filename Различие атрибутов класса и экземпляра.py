from random import randint

class Buiding:
    total = 0
    def __init__(self):
        Buiding.total += 1
        print("Buiding.total = ", Buiding.total)

for i in range(40):
    Buiding.total += 1
    print("Buiding.total = ", Buiding.total)




