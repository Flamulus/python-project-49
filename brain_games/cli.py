import prompt


def welcome_user():
    """Функция отвечает за приветсвие пользователя по имени"""
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
