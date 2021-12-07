import unittest
import planets_time from zad04.py




class planets_time_test(unittest.TestCase):
    def test_planets_time_positive(self):
        self.assertEqual(True, planets_time(5000, "Ziemia"))

    def test_planets_time_wrong_planet(self):
        self.assertRaises(Exception, planets_time, (5000, "ABC"))

    def test_planets_time_planet_tab(self):
        self.assertRaises(Exception, planets_time, (5000, []))

    def test_planets_time_planet_none(self):
        self.assertRaises(Exception, planets_time, (5000, None))

    def test_planets_time_planet_int(self):
        self.assertRaises(Exception, planets_time, (5000, 11))

    def test_planets_time_planet_float(self):
        self.assertRaises(Exception, planets_time, (5000, -3.17))

    def test_planets_time_time_str_int(self):
        self.assertEqual(True, planets_time("5000", "Ziemia"))

    def test_planets_time_time_str(self):
        self.assertRaises(Exception, planets_time, ("ABC", "Ziemia"))

    def test_planets_time_time_tab(self):
        self.assertRaises(Exception, planets_time, ([], "Ziemia"))

    def test_planets_time_time_flat(self):
        self.assertRaises(Exception, planets_time, (-117.545, "Ziemia"))

    def test_planets_time_time_none(self):
        self.assertRaises(Exception, planets_time, (None, "Ziemia"))