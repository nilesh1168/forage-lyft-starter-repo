import unittest

from tire.carrigan import Carrigan
from tire.octoprime import Octoprime

class Test_CarriganTire(unittest.TestCase):
    def test_tire_needs_servicing(self):
        tire_wear_array = [0.1, 0.3, 0.7, 1]
        tire = Carrigan(tire_wear_array)

        self.assertTrue(tire.needsServicing())

    def test_tire_needs_no_servicing(self):
        tire_wear_array = [0, 0.4, 0.8, 0.3]
        tire = Carrigan(tire_wear_array)

        self.assertFalse(tire.needsServicing())

class Test_Octoprime(unittest.TestCase):
    def test_tire_needs_servicing(self):
        tire_wear_array = [1, 0.9, 0.8, 0.3, 0]
        tire = Octoprime(tire_wear_array)

        self.assertTrue(tire.needsServicing())

    def test_tire_needs_no_servicing(self):
        tire_wear_array = [1, 0, 0.9, 0.1, 0.3]
        tire = Octoprime(tire_wear_array)

        self.assertFalse(tire.needsServicing())


if __name__ == "__main__":
    unittest.main()