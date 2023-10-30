from abc import ABC, abstractmethod
from tire.tire import Tire

class Carrigan(Tire):

    def __init__(self, tire_wear_array):
        self.tire_wear_array = tire_wear_array

    def needsServicing(self):
        for value in self.tire_wear_array:
            if value >= 0.9:
                return True
            
        return False    

    def __str__(self):
        return "Carrigan"