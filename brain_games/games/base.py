from brain_games.games.config import сolor_palette_config
from brain_games.games.communication import (
    welcome_user,
    get_user_name,
    invitation,
    congratulations_user,
    wrong_decision,
    successful_solution,
    get_answer
)


def get_rate_answer(question, correct_answer, rounds_count, name):
    answer = get_answer(question)

    if answer == str(correct_answer):
        successful_solution()
        rounds_count += 1
    else:
        wrong_decision(answer, correct_answer, name)
        rounds_count = 0

    return rounds_count


def base_game(game_condition: str, game_mechanics):
    сolor_palette_config()
    welcome_user()
    name = get_user_name()
    invitation(name=name, game_condition=game_condition)
    game_mechanics(name=name)
    congratulations_user(name=name)
