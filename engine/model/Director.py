from engine.CapuletEngine import CapuletEngine
from engine.SternmanEngine import SternmanEngine
from engine.WilloughbyEngine import WilloughbyEngine
from battery.Nubbin import Nubbin
from battery.Spindler import Spindler
from datetime import datetime, timedelta

class Director():
    def __init__(self, builder):
        self.builder = builder

    def makeCalliope(self):
        self.builder.buildEngine(CapuletEngine(30100, 0))
        self.builder.buildBattery(Spindler(datetime.now() - timedelta(365)))
        print("calliope")

    def makeGlissade(self):
        self.builder.buildEngine(WilloughbyEngine(1000, 20000))
        self.builder.buildBattery(Spindler(datetime.now() - timedelta(365*4)))

    def makePalindrome(self):
        self.builder.buildEngine(SternmanEngine(True))
        self.builder.buildBattery(Spindler(datetime.now() - timedelta(365*4)))

    def makeRorschach(self):
        self.builder.buildEngine(WilloughbyEngine(4500, 2900))
        self.builder.buildBattery(Nubbin(datetime.now() - timedelta(365*6)))

    def makeThovex(self):
        self.builder.buildEngine(CapuletEngine(10000, 9500 ))
        self.builder.buildBattery(Nubbin(datetime.now() - timedelta(365*6)))

