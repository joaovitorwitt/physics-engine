from mass_conversions import MassConversions
import unittest

mc = MassConversions()

class TestMilligramsConversion(unittest.TestCase):
    def test_negative_value(self):
        self.assertEqual(mc.convert_milligrams_to_grams(-1), "Error: Negative values are not allowed")
        self.assertEqual(mc.convert_milligrams_to_kilograms(-1), "Error: Negative values are not allowed")
        self.assertEqual(mc.convert_milligrams_to_tons(-1), "Error: Negative values are not allowed")

    def test_zero_value(self):
        self.assertEqual(mc.convert_milligrams_to_grams(0), 0.0)
        self.assertEqual(mc.convert_milligrams_to_kilograms(0), 0.0)
        self.assertEqual(mc.convert_milligrams_to_tons(0), 0.0)

    def test_invalid_value(self):
        self.assertEqual(mc.convert_milligrams_to_grams("hello"), "Error: '<' not supported between instances of 'str' and 'int'")
        self.assertEqual(mc.convert_milligrams_to_kilograms("hello"), "Error: '<' not supported between instances of 'str' and 'int'")
        self.assertEqual(mc.convert_milligrams_to_tons("hello"), "Error: '<' not supported between instances of 'str' and 'int'")



class TestGramsConversion(unittest.TestCase):
    def test_negative_value(self):
        self.assertEqual(mc.convert_grams_to_milligrams(-1), "Error: Negative values are not allowed")
        self.assertEqual(mc.convert_grams_to_kilograms(-1), "Error: Negative values are not allowed")
        self.assertEqual(mc.convert_grams_to_tons(-1), "Error: Negative values are not allowed")

    def test_zero_value(self):
        self.assertEqual(mc.convert_grams_to_milligrams(0), 0.0)
        self.assertEqual(mc.convert_grams_to_kilograms(0), 0.0)
        self.assertEqual(mc.convert_grams_to_tons(0), 0.0)

    def test_invalid_value(self):
        self.assertEqual(mc.convert_grams_to_milligrams("hello"), "Error: '<' not supported between instances of 'str' and 'int'")
        self.assertEqual(mc.convert_grams_to_kilograms("hello"), "Error: '<' not supported between instances of 'str' and 'int'")
        self.assertEqual(mc.convert_grams_to_tons("hello"), "Error: '<' not supported between instances of 'str' and 'int'")



class TestKilogramsConversion(unittest.TestCase):
    def test_negative_value(self):
        self.assertEqual(mc.convert_kilograms_to_milligrams(-1), "Error: Negative values are not allowed")
        self.assertEqual(mc.convert_kilograms_to_grams(-1), "Error: Negative values are not allowed")
        self.assertEqual(mc.convert_kilograms_to_tons(-1), "Error: Negative values are not allowed")

    def test_zero_value(self):
        self.assertEqual(mc.convert_kilograms_to_milligrams(0), 0.0)
        self.assertEqual(mc.convert_kilograms_to_grams(0), 0.0)
        self.assertEqual(mc.convert_kilograms_to_tons(0), 0.0)

    def test_invalid_value(self):
        self.assertEqual(mc.convert_kilograms_to_milligrams("hello"), "Error: '<' not supported between instances of 'str' and 'int'")
        self.assertEqual(mc.convert_kilograms_to_grams("hello"), "Error: '<' not supported between instances of 'str' and 'int'")
        self.assertEqual(mc.convert_kilograms_to_tons("hello"), "Error: '<' not supported between instances of 'str' and 'int'")



class TestTonsConversion(unittest.TestCase):
    def test_negative_value(self):
        self.assertEqual(mc.convert_tons_to_milligrams(-1), "Error: Negative values are not allowed")
        self.assertEqual(mc.convert_tons_to_grams(-1), "Error: Negative values are not allowed")
        self.assertEqual(mc.convert_tons_to_kilograms(-1), "Error: Negative values are not allowed")

    def test_zero_value(self):
        self.assertEqual(mc.convert_tons_to_milligrams(0), 0.0)
        self.assertEqual(mc.convert_tons_to_grams(0), 0.0)
        self.assertEqual(mc.convert_tons_to_kilograms(0), 0.0)

    def test_invalid_value(self):
        self.assertEqual(mc.convert_tons_to_milligrams("hello"), "Error: '<' not supported between instances of 'str' and 'int'")
        self.assertEqual(mc.convert_tons_to_grams("hello"), "Error: '<' not supported between instances of 'str' and 'int'")
        self.assertEqual(mc.convert_tons_to_kilograms("hello"), "Error: '<' not supported between instances of 'str' and 'int'")

if __name__ == "__main__":
    unittest.main()