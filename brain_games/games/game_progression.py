import random


GAME_CONDITION = 'What number is missing in the progression?'


def get_game_result():
    min_rnage_value, max_range_value = 1, 12
    min_progression_lenght, max_progression_lenght = 5, 10
    start = random.randint(min_rnage_value, max_range_value)
    step = random.randint(min_progression_lenght, max_progression_lenght)
    stop = random.randint(start + step, start + 10 * step)
    sequence = list(range(start, stop, step))

    index = random.randint(0, len(sequence) - 1)
    correct_answer = sequence[index]
    sequence[index] = ".."
    str_numbers = [str(n) for n in sequence]
    question = " ".join(str_numbers)

    return question, str(correct_answer)
