from unittest import TestCase
import unittest

from multi_fuel_dispenser.fuel import Fuel


class TestFuel(TestCase):



    def test_fuel_can_be_created_with_the_correct_inputs(self):
        self.fuel = Fuel("Petrol",550,100)

        self.assertEqual(100,self.fuel.get_quantity())
        self.assertEqual( "petrol",self.fuel.get_fuel_name())
        self.assertEqual(550,self.fuel.get_price_per_liter())


    def test_that_empty_fuel_name_will_throw_error(self):
        with self.assertRaises(ValueError):
            self.fuel = Fuel("     ",550,100)


    def test_that_if_price_is_bellow_zero_or_zero_error_will_thrown(self):
        with self.assertRaises(ValueError):
            self.fuel = Fuel("Petrol",-500,100)

        with self.assertRaises(ValueError):
            self.fuel = Fuel("Petrol",0,100)

    def test_if_quantity_is_less_than_0_or_is_0_error_will_be_thrown(self):
        with self.assertRaises(ValueError):
            self.fuel = Fuel("Petrol",550,0)

        with self.assertRaises(ValueError):
            self.fuel = Fuel("Petrol", 550, -18)

    def test_if_fuel_name_contains_digigts_error_will_be_thrown(self):
        with self.assertRaises(ValueError):
            self.fuel = Fuel("8888",550,100)


if __name__ == "__main__":
    unittest.main()