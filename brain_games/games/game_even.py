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
        number = random.randint(MIN_RANGE_VALUE, MAX_RANGE_VALUE)

        correct_answer = "yes" if number % 2 == 0 else "no"

        rounds_count = get_rate_answer(
            question=f"Question: {number}",
            correct_answer=correct_answer,
            rounds_count=rounds_count,
            name=name
        )

        if rounds_count == 0:
            raise SystemExit


def launch_game_parity_check():
    base_game(
        game_condition='Answer "yes" if the number is '
        'even, otherwise answer "no".',
        game_mechanics=game_mechanics
    )
