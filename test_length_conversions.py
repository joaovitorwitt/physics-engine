from length_conversions import LengthConversion
import unittest


class TestMillimeterConversion(unittest.TestCase):
    def test_positive_value(self):
        self.assertEqual(LengthConversion.convert_millimeter_to_centimeter(100), "10.0")

    def test_negative_value(self):
        self.assertEqual(LengthConversion.convert_millimeter_to_centimeter(-80), "Error: Negative values are not allowed")

    def test_zero_value(self):
        self.assertEqual(LengthConversion.convert_millimeter_to_centimeter(0), "0.0")

    def test_invalid_value(self):
        self.assertEqual(LengthConversion.convert_millimeter_to_centimeter("hello"), "Error: could not convert string to float: 'hello'")


class TestCentimeterConversion(unittest.TestCase):
    def test_positive_value(self):
        self.assertEqual(LengthConversion.convert_centimeter_to_millimeter(1), "10.0")
    



if __name__ == "__main__":
    unittest.main()