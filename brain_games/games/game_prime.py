import random


GAME_CONDITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_PRIME_NUMBERS, MAX_PRIME_NUMBERS = 2, 101


def game_result():
    prime_number = random.randint(MIN_PRIME_NUMBERS, MAX_PRIME_NUMBERS)
    correct_answer = "yes"
    question = prime_number

    for n in range(MIN_PRIME_NUMBERS, prime_number // 2 + 1):
        if prime_number % n == 0:
            correct_answer = "no"
            break
    return (question, str(correct_answer))
