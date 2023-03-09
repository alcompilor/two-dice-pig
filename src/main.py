#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Main module to implement the logic of the game."""

import random
import time
from textwrap import dedent
from cmd import Cmd
from computer.computer import Computer
from dice.dice import Dice
from player.player import Player
from scoreboard.scoreboard import Scoreboard
from terminal.terminal import Terminal


terminal = Terminal()


class Main(Cmd):
    """Main class."""

    prompt = ">> "

    def preloop(self):
        """Run after starting cmdloop."""
        welcome()

    def do_multiplayer(self, _):
        """Command to invoke a player vs player game."""
        player1, player2 = create_players(True)
        scoreboard, dice = init_game(player1, player2)

        terminal.display_clear()

        tracker = 1
        while not scoreboard.get_winner():  # game round loop
            # terminal.display_clear()
            terminal.display_table(scoreboard.get_scores())
            terminal.display_realtime_menu()

            if tracker == 1:
                print(f"It's {player1.get_name()}'s turn\n")
            else:
                print(f"It's {player2.get_name()}'s turn\n")

            choice = validate("Choose an option > ", "Invalid option!")

            match(choice):
                case 1:
                    terminal.display_clear()

                    cast, sum_score = dice.roll([1, 2, 3, 4, 5, 6]).values()
                    terminal.display_dice(cast)

                    if tracker == 1:

                        if (cast[0] == 1) and (cast[1] == 1):
                            scoreboard.reset_score(player1.get_name())
                            tracker = 2
                            continue
                        if (cast[0] == 1) or (cast[1] == 1):
                            tracker = 2
                            continue

                        scoreboard.update_score(
                            player1.get_name(), sum_score)
                    else:

                        if (cast[0] == 1) and (cast[1] == 1):
                            scoreboard.reset_score(player2.get_name())
                            tracker = 1
                            continue
                        if (cast[0] == 1) or (cast[1] == 1):
                            tracker = 1
                            continue

                        scoreboard.update_score(
                            player2.get_name(), sum_score)
                case 2:
                    terminal.display_clear()
                    if tracker == 1:
                        tracker = 2
                        continue

                    tracker = 1
                    continue

                case 3:
                    new_name = str(input("Enter a new name: "))
                    if tracker == 1:
                        player1.set_name(new_name)
                    else:
                        player2.set_name(new_name)
                case 4:
                    break

        end_game(scoreboard)

    def do_bot(self, _):
        """Command to invoke player vs bot game."""
        player1, player2 = create_players(False)
        scoreboard, dice = init_game(player1, player2)

        terminal.display_clear()

        terminal.display_computer_menu()
        difficulty = validate("Choose bot difficulty > ", "Invalid option!")

        computer = Computer(difficulty)
        terminal.display_clear()

        tracker = 1
        while not scoreboard.get_winner():  # game round loop
            terminal.display_table(scoreboard.get_scores())
            terminal.display_realtime_menu()

            if tracker == 2:
                terminal.display_clear()
                print(f"{player2.get_name()} turn")
                computer_decision = random.choice(
                    ['pass', 'roll', 'roll', 'roll'])
                if computer_decision == "roll":
                    print(f"{player2.get_name()} chose to roll!\n")
                    result_bot = dice.roll(computer.get_biased_list())
                    terminal.display_dice(result_bot['cast'])
                    if (result_bot['cast'][0] == 1 and
                            result_bot['cast'][1] == 1):
                        scoreboard.reset_score(player2.get_name())
                        tracker = 1
                        print(
                            f"{player2.get_name()} lost the entire score :(\n")
                        time.sleep(4)
                        terminal.display_clear()
                        continue
                    elif 1 in result_bot['cast']:
                        tracker = 1
                        print(f"{player2.get_name()} lost their turn :/\n")
                        time.sleep(4)
                        terminal.display_clear()
                        continue
                    else:
                        scoreboard.update_score(
                            player2.get_name(), result_bot['sum'])
                        terminal.display_table(scoreboard.get_scores())
                        time.sleep(4)
                        continue
                else:
                    print(f"{player2.get_name()} chose to pass..\n")
                    tracker = 1
                    time.sleep(2)
                    terminal.display_clear()
                    continue
            else:
                print("It's your turn!\n")
                choice = validate("Choose an option > ", "Invalid option!")

                match(choice):
                    case 1:
                        terminal.display_clear()
                        result = dice.roll([1, 2, 3, 4, 5, 6])
                        terminal.display_dice(result['cast'])
                        if tracker == 1:
                            if result['cast'][0] == 1 and result['cast'][1] == 1:
                                scoreboard.reset_score(player1.get_name())
                                print("You lost your entire score :(")
                                tracker = 2
                                time.sleep(4)
                                continue
                            elif 1 in result['cast']:
                                print("You lost your turn and its score :/")
                                tracker = 2
                                time.sleep(4)
                                continue
                            else:
                                scoreboard.update_score(
                                    player1.get_name(), result['sum'])
                    case 2:
                        if tracker == 1:
                            tracker = 2
                            continue
                    case 3:
                        new_name = str(input("Enter a new name: "))
                        if tracker == 1:
                            player1.set_name(new_name)
                    case 4:
                        break

                    case _:
                        continue

        end_game(scoreboard)

    def do_rules(self, _):
        """Command to display game rules."""
        terminal.display_rules()

    def do_credits(self, _):
        """Command to display project credits."""
        print(dedent("""\n
            This project is made by:
            Ahmed Abbasi & Mohamed Nour Humeidi\n
            You may also visit our github repository for more-
            information about the project:
            https://github.com/bigcbull/two-dice-pig\n"""))

    def do_exit(self, _):
        """Command to exit game."""
        print("See you later!\n")
        return True


def welcome():
    """Display game intrro (welcome)."""
    terminal.display_clear()
    terminal.display_title()
    terminal.display_intro_img()
    print("Welcome to Two-Pig Dice, where challenges abound!\n")
    terminal.display_intro_menu()
    print("Type 'help' to see available commands.\n")


def validate(prompt, error):
    """Validate inputted int."""
    while True:
        try:
            choice = int(input(prompt))
            if "difficulty" not in prompt:
                if not 0 < choice < 5:
                    raise ValueError
                return choice

            if not 0 < choice < 4:
                raise ValueError
            return choice

        except ValueError:
            print(error)
            continue


def create_players(is_multiplayer):
    """Create players for the game."""
    if is_multiplayer:
        player1_name = str(input("Enter your name (Player 1): "))

        while True:
            player2_name = str(input("Enter your name (Player 2): "))
            if player1_name == player2_name:
                print("You can't have the same name as Player 1")
                continue
            break

        player1 = Player(player1_name, False)
        player2 = Player(player2_name, False)
        return player1, player2

    else:
        player1_name = str(input("Enter your name: "))
        player2_name = random.choice(
            ["Alex (bot)", "Nadia (bot)", "Alice (bot)", "John (bot)"])

        player1 = Player(player1_name, False)
        player2 = Player(player2_name, True)
        return player1, player2


def init_game(player1, player2):
    """Init game by creating scoreboard and dice objects."""
    scoreboard = Scoreboard([player1.get_name(), player2.get_name()])
    dice = Dice()
    return scoreboard, dice


def end_game(scoreboard):
    """End game and show winner."""
    if scoreboard.get_winner():
        terminal.display_clear()
        terminal.display_winner(scoreboard.get_winner())
        terminal.display_table(scoreboard.get_scores())


if __name__ == '__main__':
    Main().cmdloop()
