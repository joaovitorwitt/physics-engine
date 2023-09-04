class TimeConversions:
    """
    A class for performing time conversions.
    """
    def convert_milliseconds_to_seconds(self, ms):
        """
        Convert milliseconds to seconds.

        Args:
            ms (float): Milliseconds to be converted. Non-negative values are expected.

        Returns:
            float: Equivalent time in seconds.

        Raises:
            ValueError: If the input value is negative.

        Example:
            >>> convert_milliseconds_to_seconds(1500)
            1.5
        """
        try:
            if ms < 0:
                raise ValueError("Negative values are not allowed")
            seconds = ms * 0.001
            return seconds
        except ValueError as ve:
            return f"Error: {ve}"
        except Exception as e:
            return f"Error: {e}"
        
        

    def convert_seconds_to_minutes(self, s):
        """
        Convert seconds to minutes.

        Args:
            s (float): Seconds to be converted. Non-negative values are expected.

        Returns:
            float: Equivalent time in minutes.

        Raises:
            ValueError: If the input value is negative.

        Example:
            >>> convert_seconds_to_minutes(120)
            2.0
        """
        try:
            if s < 0:
                raise ValueError("Negative values are not allowed")
            minutes = s / 60
            return minutes
        except ValueError as ve:
            return f"Error: {ve}"
        except TypeError as te:
            return f"Error: {te}"
        

    def convert_minutes_to_hours(self, minutes):
        """
        1 hour = 60 minutes
        """
        try:
            if minutes < 0:
                raise ValueError("Negative values are not allowed")
            hour = minutes / 60
            return hour
        except ValueError as ve:
            return f"Error: {ve}"
        except TypeError as te:
            return f"Error: {te}"
        


    def convert_hours_to_minutes(self, hours):
        """
        Convert the given value from hours to minutes.

        Args:
            hours (float or int): The value in hours to be converted to minutes.

        Returns:
            float: The equivalent value in minutes, rounded to one decimal place.

        Raises:
            ValueError: If the input is a negative value.

        Example:
            >>> convert_hours_to_minutes(2.5)
            150.0
        """
        try:
            if hours < 0:
                raise ValueError("Negative values are not allowed")
            
            minutes = hours * 60
            return round(minutes,1)
        except ValueError as ve:
            return f"Error: {ve}"
        except TypeError as te:
            return f"Error: {te}"



    def convert_minutes_to_seconds(self, minutes):
        """
        Convert the given value from minutes to seconds.

        Args:
            minutes (float or int): The value in minutes to be converted to seconds.

        Returns:
            int: The equivalent value in seconds.

        Raises:
            ValueError: If the input is a negative value.

        Example:
            >>> convert_minutes_to_seconds(2.5)
            150
        """
        try:
            if minutes < 0:
                raise ValueError("Negative values are not allowed")
            seconds = minutes * 60
            return int(seconds)
        except ValueError as ve:
            return f"Error: {ve}"
        except TypeError as te:
            return f"Error: {te}"


    def convert_seconds_to_milliseconds(self, seconds):
        """
        Convert the given value from seconds to milliseconds.

        Args:
            seconds (float or int): The value in seconds to be converted to milliseconds.

        Returns:
            int: The equivalent value in milliseconds.

        Raises:
            ValueError: If the input is a negative value.

        Example:
            >>> convert_seconds_to_milliseconds(2.5)
            2500
        """
        try:
            if seconds < 0:
                raise ValueError("Negative values are not allowed")
            milliseconds  = seconds * 1000
            return int(milliseconds)
        except ValueError as ve:
            return f"Error: {ve}"
        except TypeError as te:
            return f"Error: {te}"



    def convert_milliseconds_to_minutes(self, milliseconds):
        """
        Convert the given value from milliseconds to minutes.

        Args:
            milliseconds (float or int): The value in milliseconds to be converted to minutes.

        Returns:
            float: The equivalent value in minutes, rounded to 7 decimal places.

        Raises:
            ValueError: If the input is a negative value.

        Example:
            >>> convert_milliseconds_to_minutes(2500)
            0.0416667
        """
        try:
            if milliseconds < 0:
                raise ValueError("Negative values are not allowed")
            
            minutes = milliseconds / 60000
            return round(minutes, 7)
        except ValueError as ve:
            return f"Error: {ve}"
        except TypeError as te:
            return f"Error: {te}"




    def convert_minutes_to_milliseconds(self, minutes):
        """
        Convert the given value from minutes to milliseconds.

        Args:
            minutes (float or int): The value in minutes to be converted to milliseconds.

        Returns:
            int: The equivalent value in milliseconds.

        Raises:
            ValueError: If the input is a negative value.

        Example:
            >>> convert_minutes_to_milliseconds(2.5)
            150000
        """
        try:
            if minutes < 0:
                raise ValueError("Negative values are not allowed")
            
            milliseconds = minutes * 60000
            return int(milliseconds)
        except ValueError as ve:
            return f"Error: {ve}"
        except TypeError as te:
            return f"Error: {te}"
        


    def convert_milliseconds_to_hours(self, milliseconds):
        """
        Convert the given value from milliseconds to hours.

        Args:
            milliseconds (float or int): The value in milliseconds to be converted to hours.

        Returns:
            float: The equivalent value in hours, rounded to 9 decimal places.

        Raises:
            ValueError: If the input is a negative value.

        Example:
            >>> convert_milliseconds_to_hours(3600000)
            1.0
        """
        try:
            if milliseconds < 0:
                raise ValueError("Negative values are not allowed")
            
            hours = milliseconds / 3600000
            return round(hours, 9)
        except ValueError as ve:
            return f"Error: {ve}"
        except TypeError as te:
            return f"Error: {te}"
        


    def convert_hours_to_milliseconds(self, hours):
        """
        Convert the given value from hours to milliseconds.

        Args:
            hours (float or int): The value in hours to be converted to milliseconds.

        Returns:
            int: The equivalent value in milliseconds.

        Raises:
            ValueError: If the input is a negative value.

        Example:
            >>> convert_hours_to_milliseconds(1.5)
            5400000
        """
        try:
            if hours < 0:
                raise ValueError("Negative values are not allowed")
            
            milliseconds = hours * 3600000
            return int(milliseconds)
        except ValueError as ve:
            return f"Error: {ve}"
        except TypeError as te:
            return f"Error: {te}"
        

    def convert_seconds_to_hours(self, seconds):
        """
        Convert the given value from seconds to hours.

        Args:
            seconds (float or int): The value in seconds to be converted to hours.

        Returns:
            float: The equivalent value in hours.

        Raises:
            ValueError: If the input is a negative value.

        Example:
            >>> convert_seconds_to_hours(7200)
            2.0
        """
        try:
            if seconds < 0:
                raise ValueError("Negative values are not allowed")
            
            hours = seconds / 3600
            return round(hours, 8)
        except ValueError as ve:
            return f"Error: {ve}"
        except TypeError as te:
            return f"Error: {te}"
        


    def convert_hours_to_seconds(self, hours):
        """
        Convert the given value from hours to seconds.

        Args:
            hours (float or int): The value in hours to be converted to seconds.

        Returns:
            int: The equivalent value in seconds.

        Raises:
            ValueError: If the input is a negative value.

        Example:
            >>> convert_hours_to_seconds(1.5)
            5400
        """
        try:
            if hours < 0:
                raise ValueError("Negative values are not allowed")
            
            seconds = hours * 3600
            return int(seconds)
        except ValueError as ve:
            return f"Error: {ve}"
        except TypeError as te:
            return f"Error: {te}"
    

tc = TimeConversions()

# print(tc.convert_milliseconds_to_seconds("hello"))