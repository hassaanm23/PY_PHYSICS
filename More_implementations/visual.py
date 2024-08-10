# 2. Visualize the Pendulum's Motion We can simulate the pendulum's motion and visualize it. For this, we'll use the
# equations of motion and matplotlib to create an animation.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def pendulum_motion(length, gravity=9.81, amplitude=np.pi / 6, duration=10, frames=100):
    """
    Simulate the motion of a simple pendulum.

    :param length: Length of the pendulum in meters.
    :param gravity: Acceleration due to gravity in m/s².
    :param amplitude: Maximum angle in radians.
    :param duration: Duration of the simulation in seconds.
    :param frames: Number of frames in the animation.
    """
    from More_implementations.pendulum import calculate_period
    period = calculate_period(length, gravity)
    angular_frequency = 2 * np.pi / period

    t = np.linspace(0, duration, frames)
    theta = amplitude * np.cos(angular_frequency * t)

    x = length * np.sin(theta)
    y = -length * np.cos(theta)

    fig, ax = plt.subplots()
    line, = ax.plot([], [], 'o-', lw=2)
    time_template = 'Time = %.1fs'
    time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

    ax.set_xlim(-length - 0.5, length + 0.5)
    ax.set_ylim(-length - 0.5, length + 0.5)
    ax.set_aspect('equal')

    def init():
        line.set_data([], [])
        time_text.set_text('')
        return line, time_text

    def animate(i):
        line.set_data([0, x[i]], [0, y[i]])
        time_text.set_text(time_template % (t[i]))
        return line, time_text

    ani = animation.FuncAnimation(fig, animate, frames=frames, interval=duration * 1000 / frames, blit=True,
                                  init_func=init)

    plt.show()


# Example usage
length = 2  # meters
pendulum_motion(length)
