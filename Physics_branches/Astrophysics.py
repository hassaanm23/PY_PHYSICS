def hubble_velocity(distance, hubble_constant=70):
    """
    Calculate the velocity of a galaxy using Hubble's Law.

    :param distance: Distance to the galaxy (Mpc, megaparsecs).
    :param hubble_constant: Hubble constant (km/s/Mpc).
    :return: Velocity (km/s).
    """
    return hubble_constant * distance


# Example usage
distance = 100  # Mpc
velocity = hubble_velocity(distance)
print(f"The velocity of the galaxy is {velocity:.2f} km/s")
