import random
from operator import add, sub, mul


GAME_CONDITION = 'What is the result of the expression?'
OPERATORS = [("+", add), ("-", sub), ("*", mul)]


def get_game_result():
    min_range_value, max_range_value = 0, 12
    first_number = random.randint(min_range_value, max_range_value)
    second_number = random.randint(min_range_value, max_range_value)
    operator, mat_function = random.choice(OPERATORS)

    question = f"{first_number} {operator} {second_number}"
    correct_answer = mat_function(first_number, second_number)

    return question, str(correct_answer)
