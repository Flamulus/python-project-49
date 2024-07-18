import random


GAME_CONDITION = 'What is the result of the expression?'
MIN_RANGE_VALUE, MAX_RANGE_VALUE = 0, 12


def game_result():
    first_number = random.randint(MIN_RANGE_VALUE, MAX_RANGE_VALUE)
    second_number = random.randint(MIN_RANGE_VALUE, MAX_RANGE_VALUE)
    operator = random.choice(["+", "-", "*"])

    question = f"{first_number} {operator} {second_number}"

    match operator:
        case "+":
            correct_answer = first_number + second_number
        case "-":
            correct_answer = first_number - second_number
        case "*":
            correct_answer = first_number * second_number

    return (question, str(correct_answer))
