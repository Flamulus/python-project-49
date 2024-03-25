import prompt
import random

# Диапазон работы генератора случайных чисел
MIN_RANGE_VALUE, MAX_RANGE_VALUE = 1, 100
# Коллчиество верных ответов для завершения игры
SUCCESSFUL_RESULT = 3


def game_parity_check():
    """Консольный диалог игры"""
    сorrect_answers = 0

    print('Answer "yes" if the number is even, otherwise answer "no".')

    while сorrect_answers < SUCCESSFUL_RESULT:
        number = random.randint(MIN_RANGE_VALUE, MAX_RANGE_VALUE)
        сorrect_answer = "yes" if number % 2 == 0 else "no"

        print(f"Question: {number}")
        answer = prompt.string('Your answer: ')

        if answer == сorrect_answer:
            сorrect_answers += 1
            print("Correct!")
        else:
            сorrect_answers = 0
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{сorrect_answer}'.")
