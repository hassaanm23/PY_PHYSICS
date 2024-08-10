def lens_equation(object_distance, focal_length):
    """
    Calculate the image distance using the lens equation.

    :param object_distance: Distance from the object to the lens (cm).
    :param focal_length: Focal length of the lens (cm).
    :return: Image distance (cm).
    """
    if focal_length == 0:
        raise ValueError("Focal length cannot be zero")
    image_distance = 1 / (1 / focal_length - 1 / object_distance)
    return image_distance


# Example usage
object_distance = 10  # cm
focal_length = 5  # cm

image_distance = lens_equation(object_distance, focal_length)
print(f"The image distance is {image_distance:.2f} cm")
