def calculate_density(mass, volume):
    """
    Calculate the density of a material.

    :param mass: Mass of the material (kg).
    :param volume: Volume of the material (m³).
    :return: Density (kg/m³).
    """
    if volume == 0:
        raise ValueError("Volume cannot be zero")
    return mass / volume


# Example usage
mass = 2  # kg
volume = 0.5  # m³

density = calculate_density(mass, volume)
print(f"The density is {density:.2f} kg/m³")
