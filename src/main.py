from cmd import Cmd
from computer.computer import Computer
from dice.dice import Dice
from player.player import Player
from scoreboard.scoreboard import Scoreboard
from terminal.terminal import Terminal

class Main(Cmd):
    terminal = Terminal()
    terminal.display_title()
    terminal.display_intro_img()
    print("Welcome to Two-Pig Dice, where challenges abound!\n")
    intro = terminal.display_intro_menu()
    prompt = ">> "

    def do_multiplayer(self, arg):
        player1 = str(input("Enter your name (Player 1): "))
        player2 = str(input("Enter your name (Player 2): "))
        player1 = Player(player1, False)
        player2 = Player(player2, False)

        scoreboard = Scoreboard([player1.get_name(), player2.get_name()])
        terminal = Terminal()
        while not scoreboard.get_winner():
            terminal.display_clear()
            terminal.display_table(scoreboard.get_scores())
            terminal.display_realtime_menu()
            break


if __name__ == '__main__':
    Main().cmdloop()