from engine.Engine import Engine

class CapuletEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needsServicing(self):
        return (self.current_mileage - self.last_service_mileage) > 30000

    def __str__(self) -> str:
        return "Capulet"