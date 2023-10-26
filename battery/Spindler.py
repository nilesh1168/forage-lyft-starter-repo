from Serviceable import Serviceable
import datetime
from abc import abstractclassmethod

class Spindler(Serviceable):
    def __init__(self, lastServiceDate):
        self.lastServiceDate = lastServiceDate

    def needsServicing(self):
        service_threshold_date = self.lastServiceDate.replace(year=self.lastServiceDate.year + 2)
        if service_threshold_date < datetime.datetime.now():
            return True
        else:
            return False
        
    def __str__(self) -> str:
        return "Spindler" 