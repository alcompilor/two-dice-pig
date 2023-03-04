#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Terminal module to implement decent graphical representation."""

import os
import platform
from textwrap import dedent
import climage
import art
import tabulate


class Terminal:
    """Terminal Class."""

    def display_title(self):
        """Display game title."""
        return print(art.text2art("TWO  DICE  PIG", font="tarty3"))

    def display_intro_img(self):
        """Display game intro image."""
        return print(
            climage.convert(
                'src/graphics/img/dice_intro.jpg',
                is_unicode=True,
                width=61,
                palette="gruvbox"
            )
        )

    def display_prompt(self, text):
        """Display a prompt to enable user to input information."""
        value = input(f"{text} > ")
        return value

    def display_intro_menu(self):
        """Display game intro/main menu."""
        return print(dedent("""\
                    1. Player vs Player
                    2. Player vs Computer
                    3. View game rules
                    4. Quit\n"""))

    def display_computer_menu(self):
        """Display computer difficulty menu."""
        return print("1. Easy\n2. Moderate\n3. Hard\n")

    def display_realtime_menu(self):
        """Display a realtime menu when playing."""
        return print(dedent("""\
                    1. Roll the dice
                    2. Pass
                    3. Change name
                    4. Exit current game\n"""))

    def display_rules(self):
        """Display rules of the game."""
        return print(dedent("""\
                    Here's a brief description of how to play the game:\n
                     - The game is played by two players or against the
                     computer, and each turn consists of a player rolling
                     two six-sided dice.\n
                     - The player's score for that turn is the sum of the
                     numbers rolled on the dice.\n
                     - The player can choose to roll again and add the new
                     sum to their current score, or they can choose to end
                     their turn and keep their current score.\n
                     - If the player rolls a one on either of the dice, their
                     turn ends and their score for that turn is zero.\n
                     - If the player rolls a one on both of the dice, their
                     turn ends and their entire score during that round will
                     be lost.\n
                     - The first player to reach a predetermined winning
                     score (100 points) wins the game.\n"""))

    def display_dice(self, face1, face2):
        """Display the two dices a player gets."""
        dice1 = climage.convert(
            f'src/graphics/img/dice_{face1}.png',
            is_unicode=True,
            is_truecolor=True,
            is_256color=False,
            width=12
        )
        dice2 = climage.convert(
            f'src/graphics/img/dice_{face2}.png',
            is_unicode=True,
            is_truecolor=True,
            is_256color=False,
            width=12
        )
        return print(f'{dice1}\n{dice2}')

    def display_table(self, score_list):
        """Display a table which keeps track of the scoreboard."""
        table = score_list
        headers = ["Player", "Score"]
        return print(
            tabulate.tabulate(
                table,
                headers,
                tablefmt="heavy_outline"
            )
        )

    def display_clear(self):
        """Clear the display."""
        match (platform.system()):
            case 'Windows' | 'windows':
                os.system('cls')
            case 'Linux' | 'linux':
                os.system('clear')
            case _:
                os.system('clear')
