from engine.CapuletEngine import CapuletEngine
from engine.SternmanEngine import SternmanEngine
from engine.WilloughbyEngine import WilloughbyEngine
from battery.Nubbin import Nubbin
from battery.Spindler import Spindler
from tire.carrigan import Carrigan
from tire.octoprime import Octoprime

from datetime import datetime, timedelta

class Director():
    def __init__(self, builder):
        self.builder = builder

    def makeCalliope(self, last_service_date, current_mileage, last_service_mileage, tire_wear_array):
        self.builder.buildEngine(CapuletEngine(current_mileage, last_service_mileage))
        self.builder.buildBattery(Spindler(last_service_date))
        self.builder.buildTire(Carrigan(tire_wear_array))
        

    def makeGlissade(self, last_service_date, current_mileage, last_service_mileage, tire_wear_array):
        self.builder.buildEngine(WilloughbyEngine(current_mileage, last_service_mileage))
        self.builder.buildBattery(Spindler(last_service_date))
        self.builder.buildTire(Octoprime(tire_wear_array))

    def makePalindrome(self, last_service_date, warning_light_is_on, tire_wear_array):
        self.builder.buildEngine(SternmanEngine(warning_light_is_on))
        self.builder.buildBattery(Spindler(last_service_date))
        self.builder.buildTire(Carrigan(tire_wear_array))

    def makeRorschach(self, last_service_date, current_mileage, last_service_mileage, tire_wear_array):
        self.builder.buildEngine(WilloughbyEngine(current_mileage, last_service_mileage))
        self.builder.buildBattery(Nubbin(last_service_date))
        self.builder.buildTire(Octoprime(tire_wear_array))

    def makeThovex(self, last_service_date, current_mileage, last_service_mileage, tire_wear_array):
        self.builder.buildEngine(CapuletEngine(current_mileage, last_service_mileage ))
        self.builder.buildBattery(Nubbin(last_service_date))
        self.builder.buildTire(Octoprime(tire_wear_array))

