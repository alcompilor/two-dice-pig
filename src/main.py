import random
import time
from textwrap import dedent
from cmd import Cmd
from computer.computer import Computer
from dice.dice import Dice
from player.player import Player
from scoreboard.scoreboard import Scoreboard
from terminal.terminal import Terminal


class Main(Cmd):
    """Main class."""

    prompt = ">> "

    def preloop(self):
        """Run after starting cmdloop."""
        terminal = Terminal()
        terminal.display_clear()
        terminal.display_title()
        terminal.display_intro_img()
        print("Welcome to Two-Pig Dice, where challenges abound!\n")
        terminal.display_intro_menu()
        print("Type 'help' to see available commands.\n")

    def do_multiplayer(self, _):
        """Command to invoke a player vs player game."""
        player1 = str(input("Enter your name (Player 1): "))
        player2 = str(input("Enter your name (Player 2): "))
        player1 = Player(player1, False)
        player2 = Player(player2, False)

        scoreboard = Scoreboard([player1.get_name(), player2.get_name()])
        terminal = Terminal()
        dice = Dice()

        terminal.display_clear()
        tracker = 1
        while not scoreboard.get_winner():
            # terminal.display_clear()
            terminal.display_table(scoreboard.get_scores())
            terminal.display_realtime_menu()

            if tracker == 1:
                print(f"It's {player1.get_name()}'s turn\n")
            else:
                print(f"It's {player2.get_name()}'s turn\n")

            while True:
                try:
                    choice = int(input("Choose an option > "))
                    if not 0 < choice < 5:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid option!")
                    continue

            match(choice):
                case 1:
                    terminal.display_clear()
                    result = dice.roll([1, 2, 3, 4, 5, 6])
                    terminal.display_dice(result['cast'])
                    if tracker == 1:
                        if result['cast'][0] == 1 and result['cast'][1] == 1:
                            scoreboard.reset_score(player1.get_name())
                            tracker = 2
                            continue
                        elif 1 in result['cast']:
                            tracker = 2
                            continue
                        else:
                            scoreboard.update_score(
                                player1.get_name(), result['sum'])
                    else:
                        if result['cast'][0] == 1 and result['cast'][1] == 1:
                            scoreboard.reset_score(player2.get_name())
                            tracker = 1
                            continue
                        elif 1 in result['cast']:
                            tracker = 1
                            continue
                        else:
                            scoreboard.update_score(
                                player2.get_name(), result['sum'])
                case 2:
                    terminal.display_clear()
                    if tracker == 1:
                        tracker = 2
                        continue
                    else:
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

        if scoreboard.get_winner():
            terminal.display_clear()
            terminal.display_winner(scoreboard.get_winner())
            terminal.display_table(scoreboard.get_scores())

    def do_bot(self, _):
        """Command to invoke player vs bot game."""
        player1 = str(input("Enter your name: "))
        player2 = random.choice(
            ["Alex (Bot)", "Nadia (Bot)", "Alice (Bot)", "John (Bot)"])
        player1 = Player(player1, False)
        player2 = Player(player2, True)

        scoreboard = Scoreboard([player1.get_name(), player2.get_name()])
        terminal = Terminal()
        dice = Dice()

        terminal.display_clear()
        difficulty = None
        while True:
            try:
                terminal.display_computer_menu()
                difficulty = int(input("Choose bot difficulty > "))
                if not 0 < difficulty < 4:
                    raise ValueError
                break
            except ValueError:
                print("Invalid option!")
                continue

        computer = Computer(difficulty)

        terminal.display_clear()
        tracker = 1
        while not scoreboard.get_winner():
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
                    if result_bot['cast'][0] == 1 and result_bot['cast'][1] == 1:
                        scoreboard.reset_score(player2.get_name())
                        tracker = 1
                        print(
                            f"{player2.get_name()} lost their entire score :(\n")
                        time.sleep(4)
                        terminal.display_clear()
                        continue
                    elif 1 in result_bot['cast']:
                        tracker = 1
                        print(
                            f"{player2.get_name()} lost their turn and its score :/\n")
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
                while True:
                    try:
                        choice = int(input("Choose an option > "))
                        if not 0 < choice < 5:
                            raise ValueError
                        break
                    except ValueError:
                        print("Invalid option!")
                        continue

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

        if scoreboard.get_winner():
            terminal.display_clear()
            terminal.display_winner(scoreboard.get_winner())
            terminal.display_table(scoreboard.get_scores())

    def do_rules(self, _):
        """Command to display game rules."""
        terminal = Terminal()
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


if __name__ == '__main__':
    Main().cmdloop()
