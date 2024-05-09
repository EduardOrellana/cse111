def cels_from_fahr(fahr):
    """Convert a temprature in Fahrenheit to Celsius and
    return the Celsius temprature."""

    cels = (fahr - 32) * 5/9
    return cels