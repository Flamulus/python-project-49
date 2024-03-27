import prompt
from colorama import Fore


def welcome_user():
    print(Fore.BLUE + "Welcome to the Brain Games!")


def get_user_name() -> str:
    return prompt.string('May I have your name? ') 


def get_answer(question):
    print(Fore.BLUE + f"Question: {question}")
    answer = prompt.string('Your answer: ')
    return answer


def invitation(name: str, game_condition: str):
    print(Fore.BLUE + f"Hello, {name}!")
    print(Fore.YELLOW + game_condition)


def successful_solution():
     print(Fore.GREEN + "Correct!")


def wrong_decision(answer, сorrect_answer, name):
    print(Fore.RED + f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{сorrect_answer}'.")
    print(Fore.YELLOW + f"Let's try again, {name}!")

   
def congratulations_user(name: str):
    print(Fore.GREEN + f"Congratulations, {name}!")
