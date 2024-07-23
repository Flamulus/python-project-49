import random


GAME_CONDITION = 'Find the greatest common divisor of given numbers.'


def get_greatest_common_divisor(first_number, second_number):
    divider = min(first_number, second_number)
    while divider != 1:
        if (first_number % divider == 0
                and second_number % divider == 0):
            break
        divider -= 1
    return divider


def get_game_result():
    min_rnage_value, max_range_value = 1, 12
    first_number = random.randint(min_rnage_value, max_range_value)
    second_number = random.randint(min_rnage_value, max_range_value)

    question = f"{first_number} {second_number}"
    correct_answer = get_greatest_common_divisor(first_number, second_number)

    return question, str(correct_answer)
