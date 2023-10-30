from abc import ABC, abstractmethod
from tire.tire import Tire

class Octoprime(Tire):
    def __init__(self, tire_wear_array):
        self.tire_wear_array = tire_wear_array

    def needsServicing(self):
        sum = 0
        for value in self.tire_wear_array:
            sum+=value

        if sum >= 3:
            return True
        else:
            return False

    def __str__(self):
        return "Octoprime"