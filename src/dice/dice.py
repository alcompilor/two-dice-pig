#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Dice module."""


import random


class Dice:
    """Class for six sided dice."""

    def __init__(self):
        """Init constructor for the class dice."""
        faces = [1, 2, 3, 4, 5, 6]
        random.shuffle(faces)
        self.faces = faces

    def roll(self, faces_list):
        """Roll."""
        cast = (random.choice(faces_list), random.choice(faces_list))
        sum_cast = cast[0] + cast[1]
        return {'cast': cast, 'sum': sum_cast}
