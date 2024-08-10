# unit_convo_py - Unit Conversion for Different Quantities Handling unit conversions effectively can be very useful.
# Let’s create a more comprehensive unit conversion system for various quantities: Conversion Functions
def meters_to_kilometers(meters):
    return meters / 1000


def kilometers_to_meters(kilometers):
    return kilometers * 1000


def grams_to_kilograms(grams):
    return grams / 1000


def kilograms_to_grams(kilograms):
    return kilograms * 1000


def miles_to_kilometers(miles):
    return miles * 1.60934


def kilometers_to_miles(kilometers):
    return kilometers / 1.60934


def seconds_to_minutes(seconds):
    return seconds / 60


def minutes_to_seconds(minutes):
    return minutes * 60


def hours_to_minutes(hours):
    return hours * 60


def minutes_to_hours(minutes):
    return minutes / 60


# Example usage
distance_miles = 5
distance_km = miles_to_kilometers(distance_miles)
print(f"{distance_miles} miles is {distance_km:.2f} kilometers")
