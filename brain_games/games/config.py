from colorama import init


# Maximum number of rounds
MAX_NUMBER_ROUND = 3

# Ranges of numbers for calculations
MIN_RANGE_VALUE, MAX_RANGE_VALUE = 1, 10

# Progression ranges
MIN_PROGRESSION_LENGHT, MAX_PROGRESSION_LENGHT = 5, 10

# Prime number ranges
MIN_PRIME_NUMBERS, MAX_PRIME_NUMBERS = 2, 101


def сolor_palette_config():
    """ Configuring console output highlighting behavior """
    init(autoreset=True)
