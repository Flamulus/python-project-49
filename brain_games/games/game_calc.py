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
        operator = random.choice(["+", "-", "*"])

        match operator:
            case "+":
                correct_answer = first_number + second_number
            case "-":
                correct_answer = first_number - second_number
            case "*":
                correct_answer = first_number * second_number

        rounds_count = get_rate_answer(
            question=f"{first_number} {operator} {second_number}",
            correct_answer=correct_answer,
            rounds_count=rounds_count,
            name=name
        )

        if rounds_count == 0:
            raise SystemExit


def launch_game_calc():
    base_game(
        game_condition="What is the result of the expression?",
        game_mechanics=game_mechanics
    )
