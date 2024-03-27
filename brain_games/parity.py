import prompt
import random
from colorama import init, Fore

# Диапазон работы генератора случайных чисел
MIN_RANGE_VALUE, MAX_RANGE_VALUE = 1, 100
# Коллчиество верных ответов для завершения игры
SUCCESSFUL_RESULT = 3


def game_parity_check():
    """Консольный диалог игры"""
    rounds_count = 0

    init(autoreset=True)

    print(Fore.BLUE + "Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(Fore.BLUE + f"Hello, {name}!")
    print(Fore.YELLOW + 'Answer "yes" if the'
          ' number is even, otherwise answer "no".')

    while rounds_count < SUCCESSFUL_RESULT:
        number = random.randint(MIN_RANGE_VALUE, MAX_RANGE_VALUE)
        сorrect_answer = "yes" if number % 2 == 0 else "no"

        print(Fore.BLUE + f"Question: {number}")
        answer = prompt.string('Your answer: ')

        if answer == сorrect_answer:
            rounds_count += 1
            print(Fore.GREEN + "Correct!")
        else:
            rounds_count = 0
            print(Fore.RED + f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{сorrect_answer}'.")

    print(Fore.GREEN + f"Congratulations, {name}!")
