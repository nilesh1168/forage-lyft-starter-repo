from Car import Car
from . Builder import Builder
class CarBuilder(Builder):

    def __init__(self):
        self.car = Car()

    def buildEngine(self, engine):
        self.car.setEngine(engine)

    def buildBattery(self, battery):
        self.car.setBattery(battery)

    def buildTire(self, tire):
        self.car.setTire(tire)
        
    def build(self):
        car = self.car
        print(car)
        self.reset()
        return car
    
    def reset(self):
        self.car = Car()
        return self.car
    