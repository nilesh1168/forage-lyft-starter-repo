import Serviceable
from abc import ABC
from abc import abstractclassmethod

class Battery(ABC, Serviceable):
    def __init__(self):
        pass

    @abstractclassmethod
    def needsServicing():
        pass