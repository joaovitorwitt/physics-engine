"""  
for starters building a project like : https://pt.symbolab.com/calculator/physics/acceleration
just calculating

"""
"""
the density of a material is the mass per unit volumne
"""
def calculate_density(mass, volume):
    return mass / volume


"""
Average velocity is the ratio of the displacement X that occurs during a time interval
"""
def calculate_average_velocity(inital_position, final_position, initial_time, final_time):
    return (final_position - inital_position) / (final_time - initial_time)


"""
Average speed involves the total distance covered
"""
def calculate_average_speed(total_distance, time):
    return total_distance / time





def convert_meter_to_km(m):
    """
    This function converts a distance value from meters to kilometers. In this conversion, 1 meter is equivalent to 0.001 kilometers.

    Conversion Formula:
    1 meter = 0.001 kilometers

    To perform the conversion:
    - Take the number of meters and multiply it by 0.001.
    - The result will be the corresponding distance in kilometers.

    Example:
    convert_meter_to_km(500) returns 0.5, because 500 meters is equal to 0.5 kilometers.

    """
    return m * 0.001;


def convert_meter_to_cm(m):
    """
    this function converts a value from meters to centimeters

    Conversion Formula:
    1m = 100cm

    To perform the conversion:
    - Take the number of meters and multiply by 100
    - The result will be the corresponding value in cm

    Example: convert_meter_to_cm(10) returns 1000, because 10 meters is equal to 1000 cm
    """
    return m * 100


def convert_cm_to_meter(cm):
    """
    Conversion formula:
    1cm = 0.01 meter

    To perform the conversion:
    - take the number of centimeters and multiply by 0.01
    - since 1cm is equivalent to 0.01 meters
    """
    return cm * 0.01




def convert_mm_to_cm(mm):
    """
    Conversion formula:
    1mm = 0.1cm

    To perform the conversion:
    - take the number of mm and divide by 0.1
    - since 1mm is equivalent to 0.1 centimeters
    """
    return mm * 0.1


def convert_meter_to_cm(meter):
    """
    Conversion formula:
    1 meter = 100 cm

    To perform the conversion:
    - Take the number of meters and multiply by 100
    - since 1 meter is equivalent to 100 cm
    """
    return meter * 100


def convert_km_to_meter(km):
    """
    Conversion formula:
    1km = 1000 meter

    To perform the conversion:
    - Take the number of kilometers and multiply by 1000
    - since 1 km is equivalent to 1000 meters
    """
    return km * 1000


def convert_cm_to_mm(cm):
    """
    Conversion formula:
    1cm = 10mm

    To perform the conversion:
    - Take the number of centimeters and multiply by 10
    - since 1 centimeter is equivalent to 10 mm
    """
    return cm * 10


def convert_mm_to_km(mm):
    """
    Conversion formula:
    1mm = 0.000001 km

    To perform the conversion:
    - Take the number of centimeters and multiply by 0.000001
    - since 1mm is equivalent to 0.000001 km
    """
    # return f"{mm * 0.000001:.6f}"
    return f"{mm * 0.000001:.6}"


def convert_km_to_mm(km):
    """
    Conversion formula:
    1km = 1000000 mm

    To perform the conversion:
    - Take the number of km and multiply by 1000000 (one million)
    """
    return km * 1000000

def convert_cm_to_km(cm):
    """
    Conversion formula:
    1cm = 0.00001 km

    To perform the conversion
    - Take the number of cm and multiply by 0.00001 (1/100000)
    """
    return cm * 0.00001


def convert_km_to_cm(km):
    """
    Conversion formula:
    1km = 100000 cm

    To perform the conversion
    - Take the number of km and multiply by 100000
    """
    return km * 100000

def convert_m_to_mm(m):
    """
    Conversion formula:
    1m = 0.001 mm

    To perform the conversion
    - Take the number of meters and multiply by 0.001
    """
    return m * 1000



def convert_mm_to_m(mm):
    """
    Conversion formula:
    1mm = 1000 m

    To perform the conversion
    - Take the number of milimeters and multiply by 1000
    """
    return mm * 0.001

