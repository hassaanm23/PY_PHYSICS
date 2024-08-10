import numpy as np
import matplotlib.pyplot as plt


def ideal_gas_law(P, V, n, R=8.314):
    """
    Calculate the temperature of an ideal gas.

    :param P: Pressure in Pascals.
    :param V: Volume in cubic meters.
    :param n: Number of moles.
    :param R: Gas constant in J/(mol·K).
    :return: Temperature in Kelvin.
    """
    return (P * V) / (n * R)


def plot_ideal_gas(P_range, V, n):
    temperatures = [ideal_gas_law(P, V, n) for P in P_range]
    plt.figure(figsize=(8, 5))
    plt.plot(P_range, temperatures, label='Temperature vs. Pressure')
    plt.xlabel('Pressure (Pa)')
    plt.ylabel('Temperature (K)')
    plt.title('Ideal Gas Law')
    plt.grid(True)
    plt.legend()
    plt.show()


# Example usage
P_range = np.linspace(1e5, 2e5, 100)  # Pressure range from 100kPa to 200kPa
V = 0.0224  # Volume in cubic meters
n = 1  # Number of moles
plot_ideal_gas(P_range, V, n)
