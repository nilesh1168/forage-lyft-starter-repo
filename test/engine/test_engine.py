import unittest

from engine.CapuletEngine import CapuletEngine
from engine.SternmanEngine import SternmanEngine
from engine.WilloughbyEngine import WilloughbyEngine

class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)

        self.assertTrue(engine.needsServicing())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 0
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)

        self.assertFalse(engine.needsServicing())

    def test_engine_should_not_be_serviced_01(self):
        current_mileage = 30000
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)

        self.assertFalse(engine.needsServicing())


class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_on = True
        engine = SternmanEngine(warning_light_on)
        
        self.assertTrue(engine.needsServicing())

    def test_engine_should_not_be_serviced(self):
        warning_light_on = False
        engine = SternmanEngine(warning_light_on)
        
        self.assertFalse(engine.needsServicing())


class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        self.assertTrue(engine.needsServicing())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 0
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        self.assertFalse(engine.needsServicing())

    def test_engine_should_not_be_serviced_01(self):
        current_mileage = 60000
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        self.assertFalse(engine.needsServicing())

if __name__ == '__main__':
    unittest.main()