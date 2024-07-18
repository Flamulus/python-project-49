import random


GAME_CONDITION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_RANGE_VALUE, MAX_RANGE_VALUE = 0, 12


def game_result():
    question = random.randint(MIN_RANGE_VALUE, MAX_RANGE_VALUE)
    correct_answer = "yes" if question % 2 == 0 else "no"
    return (question, correct_answer)
