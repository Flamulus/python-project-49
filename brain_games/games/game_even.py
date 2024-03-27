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

        сorrect_answer = "yes" if number % 2 == 0 else "no"

        rounds_count = get_rate_answer(
            question=f"Question: {number}",
            сorrect_answer=сorrect_answer,
            rounds_count=rounds_count,
            name=name
        )


def launch_game_parity_check():
    base_game(
        game_condition='Answer "yes" if the number is'
        'even, otherwise answer "no".',
        game_mechanics=game_mechanics
    )


# import prompt
# import random
# from colorama import init, Fore

# from brain_games.games.config import (
#     MAX_NUMBER_ROUND,
#     MIN_RANGE_VALUE,
#     MAX_RANGE_VALUE
# )


# def launch_game_parity_check_old():
#     """Консольный диалог игры"""
#     rounds_count = 0

#     init(autoreset=True)

#     print(Fore.BLUE + "Welcome to the Brain Games!")
#     name = prompt.string('May I have your name? ')
#     print(Fore.BLUE + f"Hello, {name}!")
#     print(Fore.YELLOW + 'Answer "yes" if the'
#           ' number is even, otherwise answer "no".')

#     while rounds_count < MAX_NUMBER_ROUND:
#         number = random.randint(MIN_RANGE_VALUE, MAX_RANGE_VALUE)
#         сorrect_answer = "yes" if number % 2 == 0 else "no"

#         print(Fore.BLUE + f"Question: {number}")
#         answer = prompt.string('Your answer: ')

#         if answer == сorrect_answer:
#             rounds_count += 1
#             print(Fore.GREEN + "Correct!")
#         else:
#             rounds_count = 0
#             print(Fore.RED + f"'{answer}' is wrong answer ;(. "
#                   f"Correct answer was '{сorrect_answer}'.")
#             print(Fore.YELLOW + f"Let's try again, {name}!")

#     print(Fore.GREEN + f"Congratulations, {name}!")
