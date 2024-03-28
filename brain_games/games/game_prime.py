import random

from brain_games.games.config import (
    MAX_NUMBER_ROUND,
    MIN_PRIME_NUMBERS,
    MAX_PRIME_NUMBERS
)
from brain_games.games.base import base_game, get_rate_answer


def game_mechanics(name):
    rounds_count = 0

    while rounds_count < MAX_NUMBER_ROUND:

        prime_number = random.randint(MIN_PRIME_NUMBERS, MAX_PRIME_NUMBERS)
        correct_answer = "yes"

        for n in range(MIN_PRIME_NUMBERS, prime_number // 2 + 1):
            if prime_number % n == 0:
                correct_answer = "no"
                break

        rounds_count = get_rate_answer(
            question=prime_number,
            correct_answer=correct_answer,
            rounds_count=rounds_count,
            name=name
        )


def launch_game_prime():
    base_game(
        game_condition='Answer "yes" if given number is prime.'
        ' Otherwise answer "no".',
        game_mechanics=game_mechanics
    )
