from abc import ABC
from abc import abstractmethod

class Serviceable(ABC):
    
    @abstractmethod
    def needsServicing():
        pass
