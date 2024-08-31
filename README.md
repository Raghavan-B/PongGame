# Pong Game

This project is a recreation of the classic Pong game, implemented in Python. It provides a fun way to understand object-oriented programming (OOP) concepts through game development.

## Overview

The Pong game is a two-player game where each player controls a paddle and tries to hit the ball back and forth. The game ends when one player misses the ball, and the other player scores a point.

## Features

- **Object-Oriented Design:** The game structure is designed using OOP principles, making it modular and easy to maintain.
- **Simple Graphics:** The game utilizes the Turtle module for graphics, which makes it easy to customize.
- **Score Tracking:** The game keeps track of the score for each player.

## Installation

To run this game, you'll need Python installed on your system. You can install the required modules using the following command:

```bash
pip install turtle
```

## Usage

1. Clone this repository or download the files.
2. Run the `main.py` file to start the game.

```bash
python main.py
```

## Files Description

- **main.py:** The main file that initializes the game, handles key bindings, and manages the game loop.
- **ball.py:** Contains the `Ball` class that defines the ball's behavior, movement, and collision detection.
- **paddle.py:** Contains the `Paddle` class that defines the paddle's movement and collision with the ball.
- **score.py:** Contains the `Score` class that handles the display and updating of the players' scores.
