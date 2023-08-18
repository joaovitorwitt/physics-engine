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





# 18/08/2023 - building meter converter.....
# TODO - convert meter to km
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


print(convert_meter_to_km(9876543))
print(convert_meter_to_km(1234567))
print(convert_meter_to_km(2500))



# TODO - convert meter to cm
# TODO - convert cm to mm

# TODO - convert mm to cm
# TODO - convert cm to m
# TODO - convert m to km
