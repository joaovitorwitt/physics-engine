class MassConversions:
    """
    A class for performing mass conversions.
    """
    def convert_milligrams_to_grams(self, milligram):
        """
        Convert the given value from milligrams to grams.

        Args:
            milligram (float or int): The value in milligrams to be converted to grams.

        Returns:
            float: The equivalent value in grams.

        Raises:
            ValueError: If the input is a negative value.

        Example:
            >>> mc = MassConversions()
            >>> mc.convert_milligram_to_gram(1500)
            1.5
        """
        try:
            if milligram < 0:
                raise ValueError("Negative values are not allowed")
            
            gram = milligram / 1000
            return gram
        except ValueError as ve:
            return f"Error: {ve}"
        except TypeError as te:
            return f"Error: {te}"
        


    def convert_grams_to_milligrams(self, gram):
        """
        Convert the given value from milligrams to grams.

        Args:
            milligram (float or int): The value in milligrams to be converted to grams.

        Returns:
            float: The equivalent value in grams.

        Raises:
            ValueError: If the input is a negative value.

        Example:
            >>> MassConversions.convert_milligram_to_gram(1500)
            1.5
        """

        try:
            if gram < 0:
                raise ValueError("Negative values are not allowed")
            
            milligram = gram * 1000
            return int(milligram)
        except ValueError as ve:
            return f"Error: {ve}"
        except TypeError as te:
            return f"Error: {te}"
        

    def convert_grams_to_kilograms(self, gram):
        """
        Convert the given value from grams to kilograms.

        Args:
            gram (float or int): The value in grams to be converted to kilograms.

        Returns:
            float: The equivalent value in kilograms.

        Raises:
            ValueError: If the input is a negative value.

        Example:
            >>> mc = MassConversions()
            >>> mc.convert_gram_to_kilogram(1500)
            1.5
        """
        try:
            if gram < 0:
                raise ValueError("Negative values are not allowed")
            kilogram = gram / 1000
            return kilogram
        except ValueError as ve:
            return f"Error: {ve}"
        except TypeError as te:
            return f"Error: {te}"
        

    def convert_kilograms_to_grams(self, kilogram):
        """
        Convert the given value from kilograms to grams.

        Args:
            kilogram (float or int): The value in kilograms to be converted to grams.

        Returns:
            int: The equivalent value in grams.

        Raises:
            ValueError: If the input is a negative value.

        Example:
            >>> mc = MassConversions()
            >>> mc.convert_kilogram_to_gram(1.5)
            1500
        """
        try:
            if kilogram < 0:
                raise ValueError("Negative values are not allowed")
            
            gram = kilogram * 1000
            return int(gram)
        except ValueError as ve:
            return f"Error: {ve}"
        except TypeError as te:
            return f"Error: {te}"


    def convert_kilograms_to_tons(self, kilogram):
        """
        Convert the given value from kilograms to metric tons.

        Args:
            kilogram (float or int): The value in kilograms to be converted to metric tons.

        Returns:
            float: The equivalent value in metric tons.

        Raises:
            ValueError: If the input is a negative value.

        Example:
            >>> mc = MassConversions()
            >>> mc.convert_kilogram_to_tons(1500)
            1.5
        """
        try:
            if kilogram < 0:
                raise ValueError("Negative values are not allowed")
            
            tons = kilogram / 1000
            return tons
        except ValueError as ve:
            return f"Error: {ve}"
        except TypeError as te:
            return f"Error: {te}"


    def convert_tons_to_kilograms(self, tons):
        """
        Convert the given value from metric tons to kilograms.

        Args:
            tons (float or int): The value in metric tons to be converted to kilograms.

        Returns:
            int: The equivalent value in kilograms.

        Raises:
            ValueError: If the input is a negative value.

        Example:
            >>> mc = MassConversions()
            >>> mc.convert_tons_to_kilograms(1.5)
            1500
        """
        try:
            if tons < 0:
                raise ValueError("Negative values are not allowed")
            
            kilogram = tons * 1000
            return int (kilogram)
        except ValueError as ve:
            return f"Error: {ve}"
        except TypeError as te:
            return f"Error: {te}"
        

    def convert_milligrams_to_kilograms(self,milligram):
        """
        Convert the given value from milligrams to kilograms.

        Args:
            milligram (float or int): The value in milligrams to be converted to kilograms.

        Returns:
            float: The equivalent value in kilograms.

        Raises:
            ValueError: If the input is a negative value.

        Example:
            >>> mc = MassConversions()
            >>> mc.convert_milligram_to_kilogram(1500)
            0.0015
        """
        try:
            if milligram < 0:
                raise ValueError("Negative values are not allowed")
            
            kilogram = milligram / 1000000
            return kilogram
        except ValueError as ve:
            return f"Error: {ve}"
        except TypeError as te:
            return f"Error: {te}"
        

    def convert_kilograms_to_milligrams(self, kilograms):
        """
        Convert the given value from kilograms to milligrams.

        Args:
            kilograms (float or int): The value in kilograms to be converted to milligrams.

        Returns:
            int: The equivalent value in milligrams.

        Raises:
            ValueError: If the input is a negative value.

        Example:
            >>> mc = MassConversions()
            >>> mc.convert_kilograms_to_milligrams(1.5)
            1500000
        """
        try:
            if kilograms < 0:
                raise ValueError("Negative values are not allowed")
            
            milligrams = kilograms * 1000000
            return int(milligrams)
        except ValueError as ve:
            return f"Error: {ve}"
        except TypeError as te:
            return f"Error: {te}"


    def convert_milligrams_to_tons(self, milligrams):
        """
        Convert the given value from milligrams to metric tons.

        Args:
            milligrams (float or int): The value in milligrams to be converted to metric tons.

        Returns:
            float: The equivalent value in metric tons.

        Raises:
            ValueError: If the input is a negative value.

        Example:
            >>> mc = MassConversions()
            >>> mc.convert_milligrams_to_tons(1500000000)
            1.5
        """
        try:
            if milligrams < 0:
                raise ValueError("Negative values are not allowed")
            
            tons = milligrams / 1000000000
            return tons
        except ValueError as ve:
            return f"Error: {ve}"
        except TypeError as te:
            return f"Error: {te}"


    def convert_tons_to_milligrams(self, tons):
        """
        Convert the given value from metric tons to milligrams.

        Args:
            tons (float or int): The value in metric tons to be converted to milligrams.

        Returns:
            int: The equivalent value in milligrams.

        Raises:
            ValueError: If the input is a negative value.

        Example:
            >>> mc = MassConversions()
            >>> mc.convert_tons_to_milligrams(1.5)
            1500000000
        """
        try:
            if tons < 0:
                raise ValueError("Negative values are not allowed")
            
            milligrams = tons * 1000000000
            return int(milligrams)
        except ValueError as ve:
            return f"Error: {ve}"
        except TypeError as te:
            return f"Error: {te}"



    def convert_grams_to_tons(self, grams):
        """
        Convert the given value from grams to metric tons.

        Args:
            grams (float or int): The value in grams to be converted to metric tons.

        Returns:
            float: The equivalent value in metric tons.

        Raises:
            ValueError: If the input is a negative value.

        Example:
            >>> mc = MassConversions()
            >>> mc.convert_grams_to_tons(1500000)
            1.5
        """

        try:
            if grams < 0:
                raise ValueError("Negative values are not allowed")
            tons = grams / 1000000
            return tons
        except ValueError as ve:
            return f"Error: {ve}"
        except TypeError as te:
            return f"Error: {te}"


    def convert_tons_to_grams(self, tons):
        """
        Convert the given value from metric tons to grams.

        Args:
            tons (float or int): The value in metric tons to be converted to grams.

        Returns:
            int: The equivalent value in grams.

        Raises:
            ValueError: If the input is a negative value.

        Example:
            >>> mc = MassConversions()
            >>> mc.convert_tons_to_grams(1.5)
            1500000
        """
        try:
            if tons < 0:
                raise ValueError("Negative values are not allowed")
            grams = tons * 100000
            return int(grams)
        
        except ValueError as ve:
            return f"Error: {ve}"
        except TypeError as te:
            return f"Error: {te}"

mc = MassConversions()