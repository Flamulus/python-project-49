import prompt
from colorama import init, Fore


def run_game(modul, number_round=3):
    init(autoreset=True)

    print(Fore.BLUE + "Welcome to the Brain Games!")
    username = prompt.string("May I have your name? ")
    print(Fore.BLUE + f"Hello, {username}!")
    print(Fore.YELLOW + modul.GAME_CONDITION)

    rounds_count = 0
    while rounds_count < number_round:
        question, correct_answer = modul.game_result()
        print(Fore.BLUE + f"Question: {question}")
        answer = prompt.string("Your answer: ")

        if answer == correct_answer:
            print(Fore.GREEN + "Correct!")
            rounds_count += 1
            continue
        print(Fore.RED + f"'{answer}' is wrong answer ;(. "
                         f"Correct answer was '{correct_answer}'.")
        print(Fore.YELLOW + f"Let's try again, {username}!")
        return

    print(Fore.GREEN + f"Congratulations, {username}!")
