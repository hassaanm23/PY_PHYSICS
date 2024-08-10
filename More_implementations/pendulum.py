
#Let’s create a Python program to calculate and visualize the properties of a simple pendulum.

#1. Calculate the Period and Frequency
import math


def calculate_period(length, gravity=9.81):
    """
    Calculate the period of a simple pendulum.

    :param length: Length of the pendulum in meters.
    :param gravity: Acceleration due to gravity in m/s² (default is 9.81).
    :return: Period in seconds.
    """
    period = 2 * math.pi * math.sqrt(length / gravity)
    return period


def calculate_frequency(period):
    """
    Calculate the frequency of a simple pendulum.

    :param period: Period in seconds.
    :return: Frequency in Hz.
    """
    return 1 / period


# Example usage
length = 2  # meters
period = calculate_period(length)
frequency = calculate_frequency(period)

print(f"The period of the pendulum is {period:.2f} seconds")
print(f"The frequency of the pendulum is {frequency:.2f} Hz")
