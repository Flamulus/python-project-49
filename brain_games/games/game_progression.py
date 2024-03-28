import random

from brain_games.games.config import (
    MAX_NUMBER_ROUND,
    MIN_PROGRESSION_LENGHT,
    MAX_PROGRESSION_LENGHT,
    MIN_RANGE_VALUE,
    MAX_RANGE_VALUE
)
from brain_games.games.base import base_game, get_rate_answer


def game_mechanics(name):
    rounds_count = 0

    while rounds_count < MAX_NUMBER_ROUND:

        sequence = [random.randint(MIN_RANGE_VALUE, MAX_RANGE_VALUE)]
        step = random.randint(MIN_RANGE_VALUE, MAX_RANGE_VALUE)
        for i in range(1,
                       random.randint(MIN_PROGRESSION_LENGHT,
                                      MAX_PROGRESSION_LENGHT)
                       ):
            number = sequence[i - 1] + step
            sequence.append(number)

        index = random.randint(0, len(sequence) - 1)
        correct_answer = sequence[index]
        sequence[index] = ".."
        str_numbers = [str(n) for n in sequence]
        question = " ".join(str_numbers)

        rounds_count = get_rate_answer(
            question=question,
            correct_answer=correct_answer,
            rounds_count=rounds_count,
            name=name
        )

        if rounds_count == 0:
            raise SystemExit


def launch_game_progression():
    base_game(
        game_condition='Find the greatest common'
        ' divisor of given numbers.',
        game_mechanics=game_mechanics
    )
