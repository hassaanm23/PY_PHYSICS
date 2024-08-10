def radioactive_decay(initial_amount, half_life, time):
    """
    Calculate the remaining amount of a radioactive substance.

    :param initial_amount: Initial quantity of the substance.
    :param half_life: Half-life of the substance (time units).
    :param time: Time elapsed (time units).
    :return: Remaining quantity.
    """
    return initial_amount * (0.5 ** (time / half_life))


# Example usage
initial_amount = 1000  # grams
half_life = 5  # days
time = 15  # days

remaining_amount = radioactive_decay(initial_amount, half_life, time)
print(f"The remaining quantity is {remaining_amount:.2f} grams")
