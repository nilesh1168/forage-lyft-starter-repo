from abc import ABC, abstractmethod
class Builder(ABC):
    
    @abstractmethod
    def buildEngine():
        pass

    @abstractmethod
    def buildBattery():
        pass

    @abstractmethod
    def build():
        pass

    @abstractmethod
    def reset():
        pass
