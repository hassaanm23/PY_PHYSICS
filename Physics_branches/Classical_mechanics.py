import numpy as np
import matplotlib.pyplot as plt


def simulate_orbit(mass_sun, mass_planet, distance, velocity, days, dt):
    G = 6.67430e-11  # gravitational constant (m³/kg/s²)
    num_steps = int(days * 24 * 3600 / dt)  # Total number of time steps

    # Arrays to store the position and velocity
    x = np.zeros(num_steps)
    y = np.zeros(num_steps)
    vx = np.zeros(num_steps)
    vy = np.zeros(num_steps)

    # Initial conditions
    x[0] = distance
    vy[0] = velocity

    # Compute initial velocity to ensure a circular orbit
    vx[0] = 0  # No initial velocity in the x-direction

    for i in range(1, num_steps):
        r = np.sqrt(x[i - 1] ** 2 + y[i - 1] ** 2)
        ax = -G * mass_sun * x[i - 1] / r ** 3
        ay = -G * mass_sun * y[i - 1] / r ** 3

        # Update velocities
        vx[i] = vx[i - 1] + ax * dt
        vy[i] = vy[i - 1] + ay * dt

        # Update positions
        x[i] = x[i - 1] + vx[i] * dt
        y[i] = y[i - 1] + vy[i] * dt

    # Plot the results
    plt.figure(figsize=(8, 8))
    plt.plot(x, y)
    plt.scatter(0, 0, color='orange', label='Sun')
    plt.title('Orbit Simulation')
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.legend()
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()


# Example usage
simulate_orbit(1.989e30, 5.972e24, 1.496e11, 29780, 365, 86400)
