# 2. Simulating Physical Phenomena Simulating - physical phenomena can provide a deeper understanding of concepts. For
# instance, we can simulate projectile motion.

#Projectile Motion Simulation
import math
import matplotlib.pyplot as plt


def projectile_motion(v0, angle_deg):
    g = 9.81  # acceleration due to gravity in m/s²
    angle_rad = math.radians(angle_deg)

    # Calculate the time of flight
    t_flight = (2 * v0 * math.sin(angle_rad)) / g

    # Time intervals
    t_intervals = [i * t_flight / 100 for i in range(101)]

    # Calculate x and y positions at each time interval
    x_positions = [v0 * math.cos(angle_rad) * t for t in t_intervals]
    y_positions = [v0 * math.sin(angle_rad) * t - 0.5 * g * t ** 2 for t in t_intervals]

    # Plot the trajectory
    plt.figure(figsize=(10, 5))
    plt.plot(x_positions, y_positions)
    plt.xlabel('Distance (m)')
    plt.ylabel('Height (m)')
    plt.title(f'Projectile Motion (v0={v0} m/s, angle={angle_deg}°)')
    plt.grid(True)
    plt.show()


# Example usage
initial_velocity = 20  # m/s
angle_of_projection = 45  # degrees

projectile_motion(initial_velocity, angle_of_projection)
