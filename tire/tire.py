from abc import ABC, abstractmethod

class Tire(ABC):
    @abstractmethod
    def needsServicing(self):
        pass