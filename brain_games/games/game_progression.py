import random

GAME_CONDITION = 'What number is missing in the progression?'
MIN_RANGE_VALUE, MAX_RANGE_VALUE = 1, 12
MIN_PROGRESSION_LENGHT, MAX_PROGRESSION_LENGHT = 5, 10


def game_result():
    sequence = [random.randint(MIN_RANGE_VALUE, MAX_RANGE_VALUE)]
    step = random.randint(MIN_RANGE_VALUE, MAX_RANGE_VALUE)
    for i in range(1, random.randint(MIN_PROGRESSION_LENGHT,
                                     MAX_PROGRESSION_LENGHT)):
        number = sequence[i - 1] + step
        sequence.append(number)

    index = random.randint(0, len(sequence) - 1)
    correct_answer = sequence[index]
    sequence[index] = ".."
    str_numbers = [str(n) for n in sequence]
    question = " ".join(str_numbers)

    return (question, str(correct_answer))
