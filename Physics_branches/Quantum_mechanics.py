import numpy as np
import matplotlib.pyplot as plt


def particle_in_box(n, L, x):
    """
    Calculate the wave function for a particle in a 1D box.

    :param n: Quantum number.
    :param L: Length of the box.
    :param x: Position array.
    :return: Wave function.
    """
    return np.sqrt(2 / L) * np.sin(n * np.pi * x / L)


def plot_wave_functions(n_max, L, x):
    plt.figure(figsize=(10, 6))
    for n in range(1, n_max + 1):
        plt.plot(x, particle_in_box(n, L, x), label=f'n={n}')
    plt.title('Wave Functions for a Particle in a Box')
    plt.xlabel('x')
    plt.ylabel('Wave Function')
    plt.legend()
    plt.grid(True)
    plt.show()


# Example usage
L = 1.0  # Length of the box
x = np.linspace(0, L, 1000)
plot_wave_functions(5, L, x)
