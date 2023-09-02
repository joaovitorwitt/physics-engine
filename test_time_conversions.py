from time_conversions import TimeConversions
import unittest

tc = TimeConversions()

class TestMiilisecondsConversion(unittest.TestCase):
    def test_negative_value(self):
        self.assertEqual(tc.convert_milliseconds_to_seconds(-1), "Error: Negative values are not allowed")
        self.assertEqual(tc.convert_milliseconds_to_minutes(-1), "Error: Negative values are not allowed")
        self.assertEqual(tc.convert_milliseconds_to_hours(-1), "Error: Negative values are not allowed")

    def test_zero_value(self):
        self.assertEqual(tc.convert_milliseconds_to_seconds(0), 0.0)
        self.assertEqual(tc.convert_milliseconds_to_minutes(0), 0.0)
        self.assertEqual(tc.convert_milliseconds_to_hours(0), 0.0)

    def test_invalid_value(self):
        self.assertEqual(tc.convert_milliseconds_to_seconds("hello"), "Error: '<' not supported between instances of 'str' and 'int'")
        self.assertEqual(tc.convert_milliseconds_to_minutes("hello"), "Error: '<' not supported between instances of 'str' and 'int'")
        self.assertEqual(tc.convert_milliseconds_to_hours("hello"), "Error: '<' not supported between instances of 'str' and 'int'")



class TestSecondsConversion(unittest.TestCase):
    def test_negative_value(self):
        self.assertEqual(tc.convert_seconds_to_milliseconds(-1), "Error: Negative values are not allowed")
        self.assertEqual(tc.convert_seconds_to_minutes(-1), "Error: Negative values are not allowed")
        self.assertEqual(tc.convert_seconds_to_hours(-1), "Error: Negative values are not allowed")

    def test_zero_value(self):
        self.assertEqual(tc.convert_seconds_to_milliseconds(0), 0.0)
        self.assertEqual(tc.convert_seconds_to_minutes(0), 0.0)
        self.assertEqual(tc.convert_seconds_to_hours(0), 0.0)

    def test_invalid_value(self):
        self.assertEqual(tc.convert_seconds_to_milliseconds("hello"), "Error: '<' not supported between instances of 'str' and 'int'")
        self.assertEqual(tc.convert_seconds_to_minutes("hello"), "Error: '<' not supported between instances of 'str' and 'int'")
        self.assertEqual(tc.convert_seconds_to_hours("hello"), "Error: '<' not supported between instances of 'str' and 'int'")



class TestMinutesConversion(unittest.TestCase):
    def test_negative_value(self):
        self.assertEqual(tc.convert_minutes_to_milliseconds(-1), "Error: Negative values are not allowed")
        self.assertEqual(tc.convert_minutes_to_seconds(-1), "Error: Negative values are not allowed")
        self.assertEqual(tc.convert_minutes_to_hours(-1), "Error: Negative values are not allowed")

    def test_zero_value(self):
        self.assertEqual(tc.convert_minutes_to_milliseconds(0), 0.0)
        self.assertEqual(tc.convert_minutes_to_seconds(0), 0.0)
        self.assertEqual(tc.convert_minutes_to_hours(0), 0.0)
    
    def test_invalid_value(self):
        self.assertEqual(tc.convert_minutes_to_milliseconds("hello"), "Error: '<' not supported between instances of 'str' and 'int'")
        self.assertEqual(tc.convert_minutes_to_seconds("hello"), "Error: '<' not supported between instances of 'str' and 'int'")
        self.assertEqual(tc.convert_minutes_to_hours("hello"), "Error: '<' not supported between instances of 'str' and 'int'")



class TestHoursConversion(unittest.TestCase):
    def test_negative_value(self):
        self.assertEqual(tc.convert_hours_to_milliseconds(-1), "Error: Negative values are not allowed")
        self.assertEqual(tc.convert_hours_to_minutes(-1), "Error: Negative values are not allowed")
        self.assertEqual(tc.convert_hours_to_seconds(-1), "Error: Negative values are not allowed")

    def test_zero_value(self):
        self.assertEqual(tc.convert_hours_to_milliseconds(0), 0.0)
        self.assertEqual(tc.convert_hours_to_seconds(0), 0.0)
        self.assertEqual(tc.convert_hours_to_minutes(0), 0.0)

    def test_invalid_value(self):
        self.assertEqual(tc.convert_hours_to_milliseconds("hello"), "Error: '<' not supported between instances of 'str' and 'int'")
        self.assertEqual(tc.convert_hours_to_seconds("hello"), "Error: '<' not supported between instances of 'str' and 'int'")
        self.assertEqual(tc.convert_hours_to_minutes("hello"), "Error: '<' not supported between instances of 'str' and 'int'")



if __name__ == "__main__":
    unittest.main()