import numpy as np


def time_dilation(v, c=299792458):
    """
    Calculate time dilation effect due to special relativity.

    :param v: Velocity of the object in m/s.
    :param c: Speed of light in m/s (default is 299792458).
    :return: Time dilation factor.
    """
    return 1 / np.sqrt(1 - (v ** 2 / c ** 2))


# Example usage
velocity = 0.9 * 299792458  # 90% the speed of light
dilation = time_dilation(velocity)
print(f"The time dilation factor is {dilation:.2f}")
