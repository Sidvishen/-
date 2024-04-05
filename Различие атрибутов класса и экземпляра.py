from random import randint

class Buiding:
    total = 0
    def __init__(self):
        Buiding.total += 1
        print("Buiding.total = ", Buiding.total)

quantity = []
quantity_size = randint(0, 41)
while len(quantity) < quantity_size:
    new_Buiding = Buiding()
    quantity.append(new_Buiding)
print(Buiding.total)




