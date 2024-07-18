#!/usr/bin/env python3

from brain_games.engine import run_game
import brain_games.games.game_gcd


def main():
    run_game(modul=brain_games.games.game_gcd)


if __name__ == '__main__':
    main()
