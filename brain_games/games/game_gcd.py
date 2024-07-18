import random


GAME_CONDITION = 'Find the greatest common divisor of given numbers.'
MIN_RANGE_VALUE, MAX_RANGE_VALUE = 1, 12


def game_result():
    first_number = random.randint(MIN_RANGE_VALUE, MAX_RANGE_VALUE)
    second_number = random.randint(MIN_RANGE_VALUE, MAX_RANGE_VALUE)

    question = f"{first_number} {second_number}"

    correct_answer = min(first_number, second_number)
    while correct_answer != 1:
        if (first_number % correct_answer == 0
                and second_number % correct_answer == 0):
            break
        correct_answer -= 1

    return (question, str(correct_answer))
