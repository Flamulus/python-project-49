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


def launch_game_calc():
    base_game(
        game_condition="What is the result of the expression?",
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


# def launch_game_calc_old():
#     rounds_count = 0

#     init(autoreset=True)

#     print(Fore.BLUE + "Welcome to the Brain Games!")
#     name = prompt.string('May I have your name? ')
#     print(Fore.BLUE + f"Hello, {name}!")
#     print(Fore.YELLOW + 'What is the result of the expression?')

#     while rounds_count < MAX_NUMBER_ROUND:
#         first_number = random.randint(MIN_RANGE_VALUE, MAX_RANGE_VALUE)
#         second_number = random.randint(MIN_RANGE_VALUE, MAX_RANGE_VALUE)
#         operator = random.choice(["+", "-", "*"])

#         match operator:
#             case "+":
#                 сorrect_answer = first_number + second_number
#             case "-":
#                 сorrect_answer = first_number - second_number
#             case "*":
#                 сorrect_answer = first_number * second_number

#         print(Fore.BLUE + "Question: "
#               f"{first_number} {operator} {second_number}")
#         answer = prompt.string('Your answer: ')

#         if answer == str(сorrect_answer):
#             rounds_count += 1
#             print(Fore.GREEN + "Correct!")
#         else:
#             rounds_count = 0
#             print(Fore.RED + f"'{answer}' is wrong answer ;(. "
#                   f"Correct answer was '{сorrect_answer}'.")
#             print(Fore.YELLOW + f"Let's try again, {name}!")

#     print(Fore.GREEN + f"Congratulations, {name}!")
