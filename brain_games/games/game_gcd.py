import random

from brain_games.games.config import (
    MAX_NUMBER_ROUND,
    MIN_RANGE_VALUE,
    MAX_RANGE_VALUE
)
from brain_games.games.base import base_game, get_rate_answer


def game_mechanics(name):
    rounds_count = 0

    while rounds_count < MAX_NUMBER_ROUND:
        first_number = random.randint(MIN_RANGE_VALUE, MAX_RANGE_VALUE)
        second_number = random.randint(MIN_RANGE_VALUE, MAX_RANGE_VALUE)

        correct_answer = min(first_number, second_number)

        while correct_answer != 1:
            if (first_number % correct_answer == 0
                    and second_number % correct_answer == 0):
                break
            correct_answer -= 1

        rounds_count = get_rate_answer(
            question=f"{first_number} {second_number}",
            correct_answer=correct_answer,
            rounds_count=rounds_count,
            name=name
        )


def launch_game_gcd():
    base_game(
        game_condition='Find the greatest common'
        ' divisor of given numbers.',
        game_mechanics=game_mechanics
    )
