def bernoulli_pressure(p1, v1, h1, p2, v2, h2):
    """
    Calculate the pressure at the second point using Bernoulli's equation.

    :param p1: Pressure at the first point (Pa).
    :param v1: Velocity at the first point (m/s).
    :param h1: Height at the first point (m).
    :param p2: Pressure at the second point (Pa).
    :param v2: Velocity at the second point (m/s).
    :param h2: Height at the second point (m).
    :return: Pressure at the second point (Pa).
    """
    g = 9.81  # acceleration due to gravity (m/s²)
    pressure_2 = p1 + 0.5 * (v1 ** 2 - v2 ** 2) + g * (h1 - h2)
    return pressure_2


# Example usage
p1 = 101325  # Pressure at point 1 (Pa)
v1 = 10  # Velocity at point 1 (m/s)
h1 = 10  # Height at point 1 (m)
p2 = 0  # Pressure at point 2 (Pa, to be calculated)
v2 = 5  # Velocity at point 2 (m/s)
h2 = 5  # Height at point 2 (m)

pressure_2 = bernoulli_pressure(p1, v1, h1, p2, v2, h2)
print(f"The pressure at point 2 is {pressure_2:.2f} Pa")
