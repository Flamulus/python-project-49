import random


GAME_CONDITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime_number(number):
    min_prime_number = 2
    for n in range(min_prime_number, number // 2 + 1):
        if number % n == 0:
            return False
    return True


def get_game_result():
    min_prime_number, max_prime_number = 2, 101
    number = random.randint(min_prime_number, max_prime_number)

    question = number
    correct_answer = "yes" if is_prime_number(number) else "no"

    return question, str(correct_answer)
