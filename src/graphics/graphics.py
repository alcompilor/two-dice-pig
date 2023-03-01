#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Graphics module to implement decent graphical representation."""

import climage
import art

class Graphics:
    
    def display_title(self):
        return print(art.text2art("TWO  DICE  PIG", font="tarty3"))
    
    def display_intro_img(self):
        return print(climage.convert('src/graphics/img/dice_intro.jpg', is_unicode=True, width=61, palette="gruvbox"))
    
    def display_prompt(self, text):
        value = input(f"{text} > ")
        return value
    
    def display_intro_menu(self):
        return print("1. Player vs Player\n2. Player vs Computer\n3. Quit\n")
    
    def display_realtime_menu(self):
        return print("1. Roll the dice\n2. Pass\n3.Change name\n4. Exit current game")

    def display_dice(self, face1, face2):
        dice1 = climage.convert(f'src/graphics/img/dice_{face1}.png', is_unicode=True, is_truecolor=True, is_256color=False, width=12)
        dice2 = climage.convert(f'src/graphics/img/dice_{face2}.png', is_unicode=True, is_truecolor=True, is_256color=False, width=12)
        return print(f'{dice1}\n{dice2}')