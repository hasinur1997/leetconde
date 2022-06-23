class ParkingSystem:
    def __init__(self, big, medium, small):
        self.cars = {1: big, 2: medium, 3: small}

    def addCar(self, carType):
        if self.cars[carType] > 0:
            self.cars[carType] -= 1
            return True

        return False


park = ParkingSystem(1, 1, 5)
print(park.addCar(1))
print(park.addCar(2))
print(park.addCar(2))
print(park.addCar(3))
print(park.addCar(3))
