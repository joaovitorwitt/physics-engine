class LengthConversion:
    def convert_millimeter_to_centimeter(mm):
        """
        Conversion formula:
        1mm = 0.1cm

        To perform the conversion:
        - take the number of mm and divide by 0.1
        - since 1mm is equivalent to 0.1 centimeters
        """
        try:
            mm = float(mm)  # Convert to float, handles both strings and numbers
            if mm < 0:
                raise ValueError("Negative values are not allowed")
            cm = mm * 0.1
            return f"{cm:.1f}"
        except ValueError as ve:
            return f"Error: {ve}"
        except Exception as e:
            return f"Error: {e}"



    def convert_centimeter_to_meter(cm):
        """
        Conversion formula:
        1cm = 0.01 meter

        To perform the conversion:
        - take the number of centimeters and multiply by 0.01
        - since 1cm is equivalent to 0.01 meters
        """
        try:
            cm = float(cm)
            if cm < 0:
                raise ValueError("Negative values are not allowed")
            m = cm * 0.01
            return m
        except ValueError as ve:
            return f"Error: {ve}"
        except Exception as e:
            return f"Error: {e}"
        


    def convert_meter_to_kilometer(m):
        """
        This function converts a distance value from meters to kilometers.

        Conversion Formula:
        1 meter = 0.001 kilometers

        To perform the conversion:
        - Take the number of meters and multiply it by 0.001.
        - The result will be the corresponding distance in kilometers.

        Example:
        convert_meter_to_km(500) returns 0.5, because 500 meters is equal to 0.5 kilometers.

        """
        try:
            m = float(m)
            if m < 0:
                raise ValueError("Negative values are not allowed")
            km = f"{m * 0.001:.3f}"
            return km
        except ValueError as ve:
            return f"Error: {ve}"
        except Exception as e:
            return f"Error: {e}"



    def convert_kilometer_to_meter(km):
        """
        Conversion formula:
        1km = 1000 meter

        To perform the conversion:
        - Take the number of kilometers and multiply by 1000
        - since 1 km is equivalent to 1000 meters
        """
        try:
            km = float(km)
            if km < 0:
                raise ValueError("Negative values are not allowed")
            m = km * 1000
            return m
        except ValueError as ve:
            return f"Error: {ve}"
        except Exception as e:
            return f"Error: {e}"




    def convert_meter_to_centimeter(meter):
        """
        Conversion formula:
        1 meter = 100 cm

        To perform the conversion:
        - Take the number of meters and multiply by 100
        - since 1 meter is equivalent to 100 cm
        """
        try:
            meter = float(meter)
            if meter < 0:
                raise ValueError("Negative values are not allowed")
            cm = meter * 100
            return cm
        except ValueError as ve:
            return f"Error: {ve}"
        except Exception as e:
            return f"Error: {e}"



    def convert_centimeter_to_millimeter(cm):
        """
        Conversion formula:
        1cm = 10mm

        To perform the conversion:
        - Take the number of centimeters and multiply by 10
        - since 1 centimeter is equivalent to 10 mm
        """
        try:
            cm = float(cm)
            if cm < 0:
                raise ValueError("Negative values are not allowed")
            mm = cm * 10
            return mm
        except ValueError as ve:
            return f"Error: {ve}"
        except Exception as e:
            return f"Error: {e}"


    def convert_millimeter_to_meter(mm):
        """
        Conversion formula:
        1mm = 1000 m

        To perform the conversion
        - Take the number of milimeters and multiply by 1000
        """
        try:
            mm = float(mm)
            if mm < 0:
                raise ValueError("Negative values are not allowed")
            m = mm * 0.001
            return m
        except ValueError as ve:
            return f"Error: {ve}"
        except Exception as e:
            return f"Error: {e}"



    def convert_millimeter_to_kilometer(mm):
        """
        Conversion formula:
        1mm = 0.000001 km

        To perform the conversion:
        - Take the number of centimeters and multiply by 0.000001
        - since 1mm is equivalent to 0.000001 km
        """
        # return f"{mm * 0.000001:.6f}"
        try:
            mm = float(mm)
            if mm < 0:
                raise ValueError("Negative values are not allowed")
            km = f"{mm * 0.000001:.6}"
            return km
        except ValueError as ve:
            return f"Error: {ve}"
        except Exception as e:
            return f"Error: {e}"


    def convert_kilometer_to_millimeter(km):
        """
        Conversion formula:
        1km = 1000000 mm

        To perform the conversion:
        - Take the number of km and multiply by 1000000 (one million)
        """
        try:
            km = float(km)
            if km < 0:
                raise ValueError("Negative values are not allowed")
            mm = km * 1000000
            return mm
        except ValueError as ve:
            return f"Error: {ve}"
        except Exception as e:
            return f"Error: {e}"



    def convert_kilometer_to_centimeter(km):
        """
        Conversion formula:
        1km = 100000 cm

        To perform the conversion
        - Take the number of km and multiply by 100000
        """
        try:
            km = float(km)
            if km < 0:
                raise ValueError("Negative values are not allowed")
            cm = km * 100000
            return cm
        except ValueError as ve:
            return f"Error: {ve}"
        except Exception as e:
            return f"Error: {e}"



    def convert_centimeter_to_kilometer(cm):
        """
        Conversion formula:
        1cm = 0.00001 km

        To perform the conversion
        - Take the number of cm and multiply by 0.00001 (1/100000)
        """
        try:
            cm = float(cm)
            if cm < 0:
                raise ValueError("Negative values are not allowed")
            km = f"{cm * 0.00001:.5f}"
            return km
        except ValueError as ve:
            return f"Error: {ve}"
        except Exception as e:
            return f"Error: {e}"


    def convert_meter_to_millimeter(m):
        """
        Conversion formula:
        1m = 0.001 mm

        To perform the conversion
        - Take the number of meters and multiply by 0.001
        """
        try:
            m = float(m)
            if m < 0:
                raise ValueError("Negative values are not allowed")
            mm = m * 1000
            return mm
        except ValueError as ve:
            return f"Error: {ve}"
        except Exception as e:
            return f"Error: {e}"
        


print(LengthConversion.convert_centimeter_to_kilometer(0))