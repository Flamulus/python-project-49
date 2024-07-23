import random


GAME_CONDITION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_game_result():
    min_range_value, max_range_value = 0, 12
    question = random.randint(min_range_value, max_range_value)
    correct_answer = "yes" if question % 2 == 0 else "no"
    return question, correct_answer
