from length_conversions import LengthConversion
import unittest


class TestMillimeterConversion(unittest.TestCase):
    def test_negative_value(self):
        self.assertEqual(LengthConversion.convert_millimeter_to_centimeter(-80), "Error: Negative values are not allowed")
        self.assertEqual(LengthConversion.convert_millimeter_to_meter(-1), "Error: Negative values are not allowed")
        self.assertEqual(LengthConversion.convert_millimeter_to_kilometer(-909), "Error: Negative values are not allowed")

    def test_zero_value(self):
        self.assertEqual(LengthConversion.convert_millimeter_to_centimeter(0), "0.0")
        self.assertEqual(LengthConversion.convert_millimeter_to_meter(0), 0.0)
        self.assertEqual(LengthConversion.convert_millimeter_to_kilometer(0), "0.0")

    def test_invalid_value(self):
        self.assertEqual(LengthConversion.convert_millimeter_to_centimeter("hello"), "Error: could not convert string to float: 'hello'")
        self.assertEqual(LengthConversion.convert_millimeter_to_meter("adad"), "Error: could not convert string to float: 'adad'")
        self.assertEqual(LengthConversion.convert_millimeter_to_kilometer("dadasd"), "Error: could not convert string to float: 'dadasd'")



class TestCentimeterConversion(unittest.TestCase):
    def test_negative_value(self):
        self.assertEqual(LengthConversion.convert_centimeter_to_millimeter(-1), "Error: Negative values are not allowed")
        self.assertEqual(LengthConversion.convert_centimeter_to_millimeter(-1.9), "Error: Negative values are not allowed")
        self.assertEqual(LengthConversion.convert_centimeter_to_millimeter(-8), "Error: Negative values are not allowed")

    def test_zero_value(self):
        self.assertEqual(LengthConversion.convert_centimeter_to_millimeter(0), 0.0)
        self.assertEqual(LengthConversion.convert_centimeter_to_meter(0), 0.0)
        self.assertEqual(LengthConversion.convert_centimeter_to_kilometer(0), "0.00000")

    def test_invalid_value(self):
        self.assertEqual(LengthConversion.convert_centimeter_to_millimeter("hello"), "Error: could not convert string to float: 'hello'")
        self.assertEqual(LengthConversion.convert_centimeter_to_meter("hello"), "Error: could not convert string to float: 'hello'")
        self.assertEqual(LengthConversion.convert_centimeter_to_kilometer("hello"), "Error: could not convert string to float: 'hello'")



class TestMeterConversion(unittest.TestCase):
    def test_negative_value(self):
        self.assertEqual(LengthConversion.convert_meter_to_millimeter(-9), "Error: Negative values are not allowed")
        self.assertEqual(LengthConversion.convert_meter_to_centimeter(-9), "Error: Negative values are not allowed")
        self.assertEqual(LengthConversion.convert_meter_to_kilometer(-9), "Error: Negative values are not allowed")

    def test_zero_value(self):
        self.assertEqual(LengthConversion.convert_meter_to_millimeter(0), 0.0)
        self.assertEqual(LengthConversion.convert_meter_to_centimeter(0), 0.0)
        self.assertEqual(LengthConversion.convert_meter_to_kilometer(0), "0.000")

    def test_invalid_value(self):
        self.assertEqual(LengthConversion.convert_meter_to_millimeter("hello"), "Error: could not convert string to float: 'hello'")
        self.assertEqual(LengthConversion.convert_meter_to_centimeter("hello"), "Error: could not convert string to float: 'hello'")
        self.assertEqual(LengthConversion.convert_meter_to_kilometer("hello"), "Error: could not convert string to float: 'hello'")



class TestKilometerConversion(unittest.TestCase):
    def test_negative_value(self):
        self.assertEqual(LengthConversion.convert_kilometer_to_millimeter(-9), "Error: Negative values are not allowed")
        self.assertEqual(LengthConversion.convert_kilometer_to_centimeter(-9), "Error: Negative values are not allowed")
        self.assertEqual(LengthConversion.convert_kilometer_to_meter(-9), "Error: Negative values are not allowed")

    def test_zero_value(self):
        self.assertEqual(LengthConversion.convert_kilometer_to_millimeter(0), 0.0)
        self.assertEqual(LengthConversion.convert_kilometer_to_centimeter(0), 0.0)
        self.assertEqual(LengthConversion.convert_kilometer_to_meter(0), 0.0)

    def test_invalid_value(self):
        self.assertEqual(LengthConversion.convert_kilometer_to_millimeter("hello"), "Error: could not convert string to float: 'hello'")
        self.assertEqual(LengthConversion.convert_kilometer_to_centimeter("hello"), "Error: could not convert string to float: 'hello'")
        self.assertEqual(LengthConversion.convert_kilometer_to_meter("hello"), "Error: could not convert string to float: 'hello'")



if __name__ == "__main__":
    unittest.main()