#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Player module."""


class Player:
    """Player class."""

    def __init__(self, name, computer):
        """Init constructor for the player class."""
        self.name = str(name)
        self.computer = computer

    def is_computer(self):
        """Check whether a player is a computer or not and return bool."""
        return self.computer

    def get_name(self):
        """Return current name of the player."""
        return self.name

    def set_name(self, name):
        """Set new name for the player."""
        self.name = str(name)
