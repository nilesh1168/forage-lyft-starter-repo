from Serviceable import Serviceable

class Car(Serviceable):
    def __init__(self):
        pass

    def setEngine(self, engine):
        self.engine = engine

    def setBattery(self, battery):    
        self.battery = battery

    def needsServicing(self):
        if self.battery.needsServicing() or self.engine.needsServicing():
            return True
        else:
            return False
        
    def __str__(self) -> str:
        return "Battery : "+ self.battery.__str__() + "; Engine: "+ self.engine.__str__()
        

