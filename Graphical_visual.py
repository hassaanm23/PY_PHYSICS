#3. Graphical Visualization
#Visualizations help in understanding concepts better. We can use libraries like matplotlib for plotting graphs.

#Example: Force vs. Acceleration
import matplotlib.pyplot as plt
from unit_convo_py import grams_to_kilograms


def plot_force_vs_acceleration(mass_grams):
    mass_kg = grams_to_kilograms(mass_grams)
    accelerations = range(1, 11)  # Accelerations from 1 to 10 m/s²
    forces = [mass_kg * a for a in accelerations]

    plt.plot(accelerations, forces, marker='o')
    plt.xlabel('Acceleration (m/s²)')
    plt.ylabel('Force (N)')
    plt.title(f'Force vs. Acceleration (Mass = {mass_grams} g)')
    plt.grid(True)
    plt.show()


# Example usage
mass_grams = 500
plot_force_vs_acceleration(mass_grams)
