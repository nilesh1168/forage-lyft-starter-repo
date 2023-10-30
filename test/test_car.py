import unittest
from datetime import datetime

from engine.model.CarBuilder import CarBuilder
from engine.model.Director import Director


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.now()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        builder = CarBuilder()
        director = Director(builder)
        director.makeCalliope(last_service_date, current_mileage, last_service_mileage)
        car = builder.build()

        self.assertTrue(car.battery.needsServicing())

    def test_battery_should_not_be_serviced(self):
        today = datetime.now()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        builder = CarBuilder()
        director = Director(builder)
        director.makeCalliope(last_service_date, current_mileage, last_service_mileage)
        car = builder.build()

        self.assertFalse(car.battery.needsServicing())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        builder = CarBuilder()
        director = Director(builder)
        director.makeCalliope(last_service_date, current_mileage, last_service_mileage)
        car = builder.build()

        self.assertTrue(car.engine.needsServicing())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        builder = CarBuilder()
        director = Director(builder)
        director.makeCalliope(last_service_date, current_mileage, last_service_mileage)
        car = builder.build()

        self.assertFalse(car.engine.needsServicing())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.now()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        builder = CarBuilder()
        director = Director(builder)
        director.makeGlissade(last_service_date, current_mileage, last_service_mileage)
        car = builder.build()

        self.assertTrue(car.battery.needsServicing())

    def test_battery_should_not_be_serviced(self):
        today = datetime.now()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        builder = CarBuilder()
        director = Director(builder)
        director.makeGlissade(last_service_date, current_mileage, last_service_mileage)
        car = builder.build()

        self.assertFalse(car.battery.needsServicing())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        builder = CarBuilder()
        director = Director(builder)
        director.makeGlissade(last_service_date, current_mileage, last_service_mileage)
        car = builder.build()

        self.assertTrue(car.engine.needsServicing())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        builder = CarBuilder()
        director = Director(builder)
        director.makeGlissade(last_service_date, current_mileage, last_service_mileage)
        car = builder.build()

        self.assertFalse(car.engine.needsServicing())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.now()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False

        builder = CarBuilder()
        director = Director(builder)
        director.makePalindrome(last_service_date, warning_light_is_on)
        car = builder.build()

        self.assertTrue(car.battery.needsServicing())

    def test_battery_should_not_be_serviced(self):
        today = datetime.now()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False

        builder = CarBuilder()
        director = Director(builder)
        director.makePalindrome(last_service_date, warning_light_is_on)
        car = builder.build()

        self.assertFalse(car.battery.needsServicing())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True

        builder = CarBuilder()
        director = Director(builder)
        director.makePalindrome(last_service_date, warning_light_is_on)
        car = builder.build()

        self.assertTrue(car.engine.needsServicing())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False

        builder = CarBuilder()
        director = Director(builder)
        director.makePalindrome(last_service_date, warning_light_is_on)
        car = builder.build()

        self.assertFalse(car.engine.needsServicing())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.now()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        builder = CarBuilder()
        director = Director(builder)
        director.makeRorschach(last_service_date, current_mileage, last_service_mileage)
        car = builder.build()

        self.assertTrue(car.battery.needsServicing())

    def test_battery_should_not_be_serviced(self):
        today = datetime.now()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        builder = CarBuilder()
        director = Director(builder)
        director.makeRorschach(last_service_date, current_mileage, last_service_mileage)
        car = builder.build()

        self.assertFalse(car.battery.needsServicing())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        builder = CarBuilder()
        director = Director(builder)
        director.makeRorschach(last_service_date, current_mileage, last_service_mileage)
        car = builder.build()

        self.assertTrue(car.engine.needsServicing())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        builder = CarBuilder()
        director = Director(builder)
        director.makeRorschach(last_service_date, current_mileage, last_service_mileage)
        car = builder.build()

        self.assertFalse(car.engine.needsServicing())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.now()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        builder = CarBuilder()
        director = Director(builder)
        director.makeThovex(last_service_date, current_mileage, last_service_mileage)
        car = builder.build()

        self.assertTrue(car.battery.needsServicing())

    def test_battery_should_not_be_serviced(self):
        today = datetime.now()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        builder = CarBuilder()
        director = Director(builder)
        director.makeThovex(last_service_date, current_mileage, last_service_mileage)
        car = builder.build()

        self.assertFalse(car.battery.needsServicing())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        builder = CarBuilder()
        director = Director(builder)
        director.makeThovex(last_service_date, current_mileage, last_service_mileage)
        car = builder.build()

        self.assertTrue(car.engine.needsServicing())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        builder = CarBuilder()
        director = Director(builder)
        director.makeThovex(last_service_date, current_mileage, last_service_mileage)
        car = builder.build()

        self.assertFalse(car.engine.needsServicing())


if __name__ == '__main__':
    unittest.main()
