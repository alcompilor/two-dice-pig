#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Main module to implement the logic of the game."""

# pylint: disable=import-error
import random
import time
from textwrap import dedent
from cmd import Cmd
from computer.computer import Computer
from dice.dice import Dice
from player.player import Player
from scoreboard.scoreboard import Scoreboard
from terminal.terminal import Terminal


terminal = Terminal()  # global usage


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

        terminal.display_clear()  # clear terminal for better experience

        tracker = 1  # keep track of turns, player1 = 1, player2 = 2
        while not scoreboard.get_winner():  # game round loop
            terminal.display_table(scoreboard.get_scores())
            terminal.display_realtime_menu()

            if tracker == 1:
                print(f"It's {player1.get_name()}'s turn\n")
            else:
                print(f"It's {player2.get_name()}'s turn\n")

            choice = validate_option("Choose an option > ", "Invalid option!")

            match(choice):  # logic based on option
                case 1:
                    terminal.display_clear()

                    cast, sum_score = dice.roll(dice.faces).values()
                    terminal.display_dice(cast)  # display dice

                    if tracker == 1:  # if it's player1 turn

                        if (cast[0] == 1) and (cast[1] == 1):
                            scoreboard.reset_score(
                                player1.get_name())
                            tracker = 2  # give turn to player2
                            continue

                        if (cast[0] == 1) or (cast[1] == 1):
                            tracker = 2
                            continue

                        scoreboard.update_score(
                            player1.get_name(), sum_score)
                    else:  # if it's player2 turn

                        if (cast[0] == 1) and (cast[1] == 1):
                            scoreboard.reset_score(player2.get_name())
                            tracker = 1  # give turn to player1
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
                    new_name = validate_name(
                        "Enter a new name: ",
                        "Name is too short or already in use",
                        scoreboard)

                    if tracker == 1:  # change player1 name
                        scoreboard.update_name(
                            player1.get_name(), new_name)
                        player1.set_name(new_name)

                    if tracker == 2:  # change player2 name
                        scoreboard.update_name(
                            player2.get_name(), new_name)
                        player2.set_name(new_name)

                    terminal.display_clear()
                case 4:
                    break

        end_game(scoreboard)  # finish game

    def do_bot(self, _):
        """Command to invoke player vs bot game."""
        player1, player2 = create_players(False)
        scoreboard, dice = init_game(player1, player2)

        terminal.display_clear()

        terminal.display_computer_menu()
        difficulty = validate_option(
            "Choose bot difficulty > ", "Invalid option!")

        bot = Computer(difficulty)  # create bot
        terminal.display_clear()

        tracker = 1  # keep track of turns, player = 1, bot = 2
        while not scoreboard.get_winner():  # game round loop
            terminal.display_table(scoreboard.get_scores())
            terminal.display_realtime_menu()

            if tracker == 2:  # if it's the bot's turn
                terminal.display_clear()
                print(f"{player2.get_name()} turn")

                # decide whether to roll or pass
                bot_decision = random.choice(bot.get_decision_list())

                if bot_decision == "roll":  # if bot rolls

                    print(f"{player2.get_name()} chose to roll!\n")
                    cast, sum_score = dice.roll(bot.get_biased_list()).values()

                    terminal.display_dice(cast)

                    if (cast[0] == 1) and (cast[1] == 1):
                        scoreboard.reset_score(player2.get_name())
                        tracker = 1
                        print(
                            f"{player2.get_name()} lost the entire score :(\n")
                        time.sleep(4)  # improves game flow
                        terminal.display_clear()
                        continue

                    if (cast[0] == 1) or (cast[1] == 1):
                        tracker = 1
                        print(f"{player2.get_name()} lost their turn :/\n")
                        time.sleep(4)
                        terminal.display_clear()
                        continue

                    scoreboard.update_score(
                        player2.get_name(), sum_score)
                    terminal.display_table(scoreboard.get_scores())
                    time.sleep(4)
                    continue

                else:  # if bot passes
                    print(f"{player2.get_name()} chose to pass..\n")
                    tracker = 1
                    time.sleep(2)
                    terminal.display_clear()
                    continue
            else:  # if it's the player's turn
                print("It's your turn!\n")
                choice = validate_option(
                    "Choose an option > ", "Invalid option!")

                match(choice):  # logic based on option
                    case 1:
                        terminal.display_clear()

                        cast, sum_score = dice.roll(dice.faces).values()
                        terminal.display_dice(cast)

                        if tracker == 1:

                            if (cast[0] == 1) and (cast[1] == 1):
                                scoreboard.reset_score(player1.get_name())
                                print("You lost your entire score :(")
                                tracker = 2
                                time.sleep(4)
                                continue

                            if (cast[0] == 1) or (cast[1] == 1):
                                print("You lost your turn and its score :/")
                                tracker = 2
                                time.sleep(4)
                                continue

                            scoreboard.update_score(
                                player1.get_name(), sum_score)
                    case 2:
                        if tracker == 1:
                            tracker = 2
                            continue
                    case 3:
                        new_name = validate_name(
                            "Enter a new name: ",
                            "Name is too short or already in use",
                            scoreboard)

                        if tracker == 1:
                            scoreboard.update_name(
                                player1.get_name(), new_name)
                            player1.set_name(new_name)

                        terminal.display_clear()

                    case 4:
                        break

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


def validate_option(prompt, error):
    """Validate inputted int."""
    while True:
        try:
            choice = int(input(prompt))
            if "difficulty" not in prompt:  # for in-game menu
                if not 0 < choice < 5:
                    raise ValueError
                return choice

            if not 0 < choice < 4:  # for choosing bot difficulty
                raise ValueError
            return choice

        except ValueError:
            print(error)
            continue


def validate_name(prompt, error, scoreboard):
    """Validate name before changing it."""
    forbidden_names = ["Alex (bot)", "Nadia (bot)",
                       "Alice (bot)", "John (bot)"]  # used by bot
    while True:
        name = str(input(prompt))
        if not scoreboard:  # when creating new players
            if (len(name) < 1) or (name in forbidden_names):
                print(error)
                continue
        else:  # when changing name during game
            if (len(name) < 1 or scoreboard.get_player(name) or
                    name in forbidden_names):
                print(error)
                continue
        return name


def create_players(is_multiplayer):
    """Create players for the game."""
    if is_multiplayer:  # player vs player
        player1_name = validate_name(
            "Enter your name (Player 1): ",
            "Name too short",
            scoreboard=False)

        while True:  # validates it's not same as player1 name
            player2_name = validate_name(
                "Enter your name (Player 2): ",
                "Name too short or already in use",
                scoreboard=False)

            if player1_name == player2_name:
                print("Name can't be same as Player 2")
                continue
            break

        player1 = Player(player1_name, False)
        player2 = Player(player2_name, False)
        return player1, player2

    else:  # player vs bot
        player1_name = validate_name(
            "Enter your name (Player 1): ",
            "Name too short or can't be used",
            scoreboard=False)

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
