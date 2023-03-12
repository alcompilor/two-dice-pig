# 🎲 Two-Dice Pig Game

| ![license badge](https://img.shields.io/badge/license%20-MIT-green) | ![coverage badge](https://img.shields.io/badge/coverage%20-99%25-success) | ![pylint badge](https://img.shields.io/badge/pylint-passed-blue) | ![flake8 badge](https://img.shields.io/badge/flake8-passed-blue) |
| :-----------------------------------------------------------------: | :-----------------------------------------------------------------------: | :--------------------------------------------------------------: | :--------------------------------------------------------------: |

Here's a brief description of how to play the game:

- The game is played by two players or against the computer, and each turn consists of a player rolling two six-sided dice.

- The player's score for that turn is the sum of the numbers rolled on the dice.

- The player can choose to roll again and add the new sum to their current score, or they can choose to end their turn and keep their current score.

- If the player rolls a one on either of the dice, their turn ends and their score for that turn is zero.

- If the player rolls a one on both of the dice, their turn ends and their entire score during that round will be lost.

- The first player to reach a predetermined winning score (100 points) wins the game.

## ⚠️ Requirements

**python** - >= v3.10

**make** - You might want to use Chocolatey in order to install make on Windows

**pip** - Usually comes with Python but you might need to manually install it

**graphviz** - Optional and only required in case you want to generate UML for the codebase

**_Important:_** _Use just native terminal/cmd to launch the game; avoid using IDEs._

## 🎮 Get Started

_Follow the steps below to start playing the game_

Clone the game

```bash
  git clone https://github.com/bigcbull/two-dice-pig.git
```

Go to the game directory

```bash
  cd two-dice-pig
```

Create and activate a virtual environment - (Linux/macOS)

```bash
  python -m venv venv && source ./venv/bin/activate
```

Create and activate a virtual environment - (Windows)

```bash
  python -m venv venv && .\venv\Scripts\activate
```

Install required dependencies

```bash
  make init
```

Run the game

```bash
  make play
```

Don't forget to deactivate the virtual environment when done

```bash
  deactivate
```

**_Important:_** _Always reactivate the virtual environment before playing._

**_Note:_** _Running 'make' without specifying any args will result in 'make init' being invoked._

## ⚙️ Running Tests - for development purposes

To execute tests and linters, run the following command

```bash
  make test dir=./src/<package>
```

Example - To run tests and linters on the player package one can do the following:

```bash
  make test dir=./src/player
```

As a result one would get:

![Linting and Unit testing](https://i.imgur.com/ECKY5Ck.png)

**_Note:_** _Windows users must use a bash terminal such as [git bash](https://gitforwindows.org/) in order for this to work correctly._

## 📃 Documentation - for development purposes

To view documentation for specific module, run the following command

```bash
  make doc module=./src/<package>/<module>.py
```

Example - To view documentation for the player module in the player package one can do the following:

```bash
  make doc module=./src/player/player.py
```

As a result one would get:

![Documentation for modules](https://i.imgur.com/TyDxR0x.png)

**_Note:_** _Windows users might need to use a bash terminal such as [git bash](https://gitforwindows.org/) in order for this to work correctly._

## 📝 UML - for development purposes

To generate UML for the codebase, simply run the following command

```bash
  make uml
```

After running the command, UMLs will be generated in the root directory.

**_Note:_** _Windows users might need to use a bash terminal such as [git bash](https://gitforwindows.org/) in order for this to work correctly._

## 🤖 Computer Intelligence - for development purposes

We had the opportunity to implement a dice game that required randomness in its gameplay mechanics. However, we wanted to create a unique gameplay experience by **biasing the probabilities of certain outcomes** to make the game more exciting and unpredictable.

In order to accomplish this, we used **biased probability to limit the possibility that particular outcomes would occur while rolling the dice.**

For instance, we made it more likely for bots to win more points in the hard level by **raising the likelihood that they would roll a higher number on the die.** To make it harder for players to defeat bots, we **simultaneously decreased the likelihood of a bot rolling a low number.** The bot's ability to select whether to roll or pass the dice was likewise handled using the same method.

By introducing these biased probabilities, we were able to create a gameplay experience that was both challenging and unpredictable.

It is important to note that introducing biased probability into a game **requires careful consideration and testing to ensure that the gameplay remains fair and balanced.** If the probabilities are too heavily skewed, the game may become unbalanced and lose its appeal to players. Therefore, it is important to carefully adjust the probabilities to create a unique gameplay experience while maintaining fairness and balance.

Overall, using biased probability to affect randomness in a dice game can be an effective way to create a more engaging and exciting gameplay experience. With careful planning and testing, it is possible to introduce biased probability in a way that is both enjoyable and fair for players.
