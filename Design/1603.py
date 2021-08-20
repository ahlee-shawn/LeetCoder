class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.bigSpace = big
        self.mediumSpace = medium
        self.smallSpace = small

    def addCar(self, carType: int) -> bool:
        if carType == 1: # Big
            if self.bigSpace == 0:
                return False
            else:
                self.bigSpace -= 1
                return True
        if carType == 2: # Medium
            if self.mediumSpace == 0:
                return False
            else:
                self.mediumSpace -= 1
                return True
        if carType == 3: # Small
            if self.smallSpace == 0:
                return False
            else:
                self.smallSpace -= 1
                return True


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)