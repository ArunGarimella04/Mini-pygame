# Runner Game

A simple 2D runner game built using Python and the PyGame library. The game features a main screen, background music, animated obstacles, and a scoring system.

---

## Features

- **Main Screen**: A welcoming screen with background music and instructions to start the game.
- **Gameplay**:
  - Player can jump and move left or right to avoid obstacles.
  - Animated obstacles (snails and flies) move across the screen.
  - Gravity and collision detection are implemented.
- **Scoring System**:
  - Score increases over time, with higher increments as the score gets higher.
  - Final score is displayed on the game-over screen.
- **Background Music**:
  - Separate background music for the login screen and gameplay.
- **Game Over Screen**:
  - Displays the final score and options to restart or return to the login screen.

---

## How to Play

1. **Start the Game**:
   - Run the script using Python.
   - On the login screen, press `Enter` to start the game.

2. **Controls**:
   - `Space`: Jump.
   - `Right Arrow` or `D`: Move right.
   - `Left Arrow` or `A`: Move left.
   - `Down Arrow` or `S`: Increase gravity (fall faster).
   - `Escape`: Return to the login screen.

3. **Objective**:
   - Avoid obstacles (snails and flies) and survive as long as possible to achieve a high score.

4. **Game Over**:
   - When the player collides with an obstacle, the game ends.
   - Press `Space` to restart or `Escape` to return to the login screen.

---

## Installation

1. Clone this repository or download the source code.
2. Install the required dependencies:
     pip install pygame
3. Run the game:
     python app.py

## Dependencies
- Python 3.8+
- PyGame 2.0+

## Credits
  Game Development: Garimella Arun

## Assets:
- Background music and sound effects from free sounds.
- Game graphics created or sourced from free asset libraries.
