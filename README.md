# Snake Game - Turtle Library

## Overview

This is a simple Snake game built using Python's `turtle` library. The project is based on Dr. Angela Yu's course and covers fundamental concepts in game development such as object-oriented programming, event-driven movement, and collision detection.

## Features

- **Snake Movement**: The snake moves automatically in a chosen direction.
- **User Controls**: Use the arrow keys to control the snake's direction.
- **Food Collision**: The snake grows when it eats food.
- **Scoreboard**: Displays the current score and updates when food is consumed.
- **Wall Collision Detection**: The game ends if the snake hits a wall.
- **Self-Collision Detection**: The game ends if the snake collides with itself.

## Requirements

- Python 3.11.7
- Turtle library (built into Python)

## How to Run

1. Ensure Python is installed on your system.
2. Download or clone this repository.
3. Run the `main.py` script in a Python environment.

```sh
python main.py
```

## Project Breakdown

### 1. Creating the Snake Body

- Initialize a three-segment snake using `turtle.Turtle()` objects.
- Position each segment in a line to form the initial snake body.

### 2. Moving the Snake

- Continuously move the snake forward by updating segment positions.
- Implement a loop to keep the snake moving automatically.

### 3. Controlling the Snake

- Capture user input using `turtle.listen()` and `turtle.onkey()`.
- Allow movement using arrow keys (Up, Down, Left, Right).
- Restrict the snake from reversing direction.

### 4. Detecting Collision with Food

- Generate food at a random location on the screen.
- Detect when the snake's head reaches the food.
- Increase the snake length and update the score.

### 5. Creating a Scoreboard

- Display the score at the top of the screen.
- Update the score when food is consumed.
- Reset the game or end when collision occurs.

### 6. Detecting Collision with Walls

- Check if the snake's head crosses the screen boundary.
- End the game or restart when a wall collision is detected.

### 7. Detecting Collision with Itself

- Check if the snake's head collides with its own body.
- End the game if a self-collision is detected.

## Possible Enhancements

- Add sound effects for eating and collisions.
- Implement different game difficulty levels.
- Save high scores.
- Add power-ups or obstacles for an extra challenge.

## Credits

This project is part of Dr. Angela Yu's Python course and follows her structured approach to game development using the `turtle` module.

Enjoy coding and happy gaming! 🎮🐍
