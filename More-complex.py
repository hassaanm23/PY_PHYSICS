#4. Handling More Complex Physical Laws
#For more advanced physics concepts, let’s consider the laws of thermodynamics or fluid mechanics.

#Example: Ideal Gas Law
def ideal_gas_law(P, V, n, R=8.314):
    # P: pressure in Pascals
    # V: volume in cubic meters
    # n: number of moles
    # R: gas constant, default is 8.314 J/(mol·K)
    T = (P * V) / (n * R)
    return T


# Example usage
pressure = 101325  # Pascals
volume = 0.0224  # cubic meters (22.4 liters)
moles = 1  # moles of gas

temperature = ideal_gas_law(pressure, volume, moles)
print(f"The temperature is {temperature:.2f} K")
