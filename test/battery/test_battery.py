import unittest
from datetime import datetime

from battery.Nubbin import Nubbin
from battery.Spindler import Spindler


class TestNubbin(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.now()
        last_service_date = today.replace(year=today.year - 5)
        
        battery = Nubbin(last_service_date)

        self.assertTrue(battery.needsServicing())

    def test_battery_should_not_be_serviced(self):
        today = datetime.now()
        last_service_date = today.replace(year=today.year - 1)
        
        battery = Nubbin(last_service_date)
        self.assertFalse(battery.needsServicing())


class TestSpindler(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.now()
        last_service_date = today.replace(year=today.year - 3)

        battery = Spindler(last_service_date)

        self.assertTrue(battery.needsServicing())

    def test_battery_should_not_be_serviced(self):
        today = datetime.now()
        last_service_date = today.replace(year=today.year - 2)

        battery = Spindler(last_service_date)

        self.assertFalse(battery.needsServicing())

if __name__ == '__main__':
    unittest.main()
