from Serviceable import Serviceable
from abc import abstractclassmethod


class Engine(Serviceable):
    @abstractclassmethod
    def needsServicing():
        pass