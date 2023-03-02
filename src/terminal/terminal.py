#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Terminal module to implement decent graphical representation."""

import os
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
        return print("1. Player vs Player\n2. Player vs Computer\n3. Quit\n")

    def display_computer_menu(self):
        """Display computer difficulty menu."""
        return print("1. Easy\n2. Moderate\n3. Hard\n")

    def display_realtime_menu(self):
        """Display a realtime menu when playing."""
        return print("1. Roll the dice\n2. Pass\n3.Change name\n\
                     4. Exit current game\n")

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
        return os.system('cls' if os.name == 'nt' else 'clear')
