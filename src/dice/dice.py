#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Dice class."""


import random


class Dice:
    """six sided dice."""

    def roll(self, faces_list):
        """Roll."""
        cast = (random.choice(faces_list), random.choice(faces_list))
        sum_cast = cast[0] + cast[1]
        return {'cast': cast, 'sum': sum_cast}
