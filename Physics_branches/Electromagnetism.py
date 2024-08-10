import numpy as np
import matplotlib.pyplot as plt


def electric_field(q, pos_charge, x, y):
    k = 8.9875517923e9  # Coulomb's constant
    rx = x - pos_charge[0]
    ry = y - pos_charge[1]
    r = np.sqrt(rx ** 2 + ry ** 2)
    E = k * q / r ** 2
    Ex = E * (rx / r)
    Ey = E * (ry / r)
    return Ex, Ey


def plot_electric_field(charges, positions, grid_size=10):
    x = np.linspace(-grid_size, grid_size, 100)
    y = np.linspace(-grid_size, grid_size, 100)
    X, Y = np.meshgrid(x, y)

    Ex, Ey = np.zeros_like(X), np.zeros_like(Y)

    for charge, pos in zip(charges, positions):
        ex, ey = electric_field(charge, pos, X, Y)
        Ex += ex
        Ey += ey

    plt.figure(figsize=(8, 8))
    plt.streamplot(X, Y, Ex, Ey, density=1.5, color='b')
    plt.scatter(*zip(*positions), color='r', s=100, label='Charges')
    plt.title('Electric Field')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()


# Example usage
charges = [1e-9, -1e-9]  # Charges in Coulombs
positions = [(1, 1), (-1, -1)]  # Positions of the charges
plot_electric_field(charges, positions)
