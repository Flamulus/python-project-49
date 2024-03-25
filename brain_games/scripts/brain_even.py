#!/usr/bin/env python3

import prompt

from brain_games.parity import game_parity_check


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    game_parity_check()
    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
