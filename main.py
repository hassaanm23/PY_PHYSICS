def grams_to_kilograms(g):
    """This function converts grams to kilograms"""
    if g < 0:
        raise ValueError("Mass cannot be negative")
    return g / 1000


def calculate_momentum(mass_g, velocity):
    if velocity < 0:
        raise ValueError("Velocity cannot be negative")
    mass_kg = grams_to_kilograms(mass_g)
    return mass_kg * velocity


'''try:
    mass_g = float(input("Enter mass in grams: "))
    velocity = float(input("Enter velocity in m/s: "))
    momentum = calculate_momentum(mass_g, velocity)
    print(f"The momentum is {momentum} kg·m/s")
except ValueError as e:
    print(e)'''


def calculate_kinetic_energy(mass_g, velocity):
    """"#kinetic_energy = calculate_kinetic_energy(mass_grams, velocity)\n#print(f"The kinetic energy is {
    kinetic_energy} Joules")"""
    mass_kg = grams_to_kilograms(mass_g)
    return 0.5 * mass_kg * velocity ** 2  # K.E = 1/2 * M * (V * V) #squared


def calculate_force(mass_g, acceleration):
    """force = calculate_force(mass_grams, acceleration)\nprint(f"The force is {force} Newtons")"""
    mass_kg = grams_to_kilograms(mass_g)
    force = mass_kg * acceleration  # F = MA(mass x acceleration)
    return force
