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
        dice = Dice()
        
        tracker = 1
        while not scoreboard.get_winner():
            # terminal.display_clear()
            terminal.display_table(scoreboard.get_scores())
            terminal.display_realtime_menu()

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
                    print(tracker)
                    result = dice.roll([1, 2, 3, 4, 5, 6])
                    terminal.display_dice(result['cast'])
                    if tracker == 1:
                        if 1 in result['cast']:
                            scoreboard.reset_score(player1.get_name())
                        else:
                            scoreboard.update_score(player1.get_name(), result['sum'])
                    else:
                        if 1 in result['cast']:
                            scoreboard.reset_score(player2.get_name())
                        else:
                            scoreboard.update_score(player2.get_name(), result['sum'])
                case 2:
                    if tracker == 1:
                        tracker = 2
                        
                    else:
                        tracker = 1
                        
                case 3:
                    print("3")
                case 4:
                    print("4")



if __name__ == '__main__':
    Main().cmdloop()