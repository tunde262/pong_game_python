# PONG Game with Pygame

A classic **PONG** game built using **Pygame**. Includes 2-player local gameplay, paddle controls, a scoring system, and collision detection. The program also includes optional web hosting support using **asyncio**.

![thumbnail](https://github.com/tunde262/pong_game_python/blob/main/assets/thumbnail.png?raw=true)

## Features
- Classic **PONG** gameplay for two players.
- Smooth paddle and ball movement with realistic collision mechanics.
- Scoring system displayed on the screen.
- Restart and play functionalities using keyboard controls.
- Optimized to run at **60 FPS** for smooth visuals.
- **Optional Web Hosting** on the web using asyncio compatibility with the Pygbag library..

---

## Requirements

- Python 3.8+, recommended for the following reasons:
  1. **Enhanced `asyncio` Support**: The project uses `asyncio.run()` for the optional web-hosting feature, which simplifies asynchronous execution.
  2. **Compatibility with Pygbag**: Pygbag, used for web hosting, requires Python 3.8+.
- Pygame (install via `pip install pygame`)
- (Optional) Pygbag for web hosting

## Installation

1. **Clone the Repository**:
   
   ```bash
   git clone https://github.com/tunde262/pong_game_python.git
   cd pong_game_python
   ```
   
3. **Install Dependencies**: Ensure you have Python 3.8+ installed. Then, install the required libraries:
   
   ```bash
   pip install pygame
   ```

4. **Run the Game**:
   
   ```bash
   python main.py
   ```

---

## Web Hosting (Optional)

This project supports optional web hosting using `asyncio` and the **Pygbag** library.

1. **Install the Pygbag library**:
   ```bash
   pip install pygbag
   ```
   
2. **Compile and host the game**:
   ```bash
   pygbag main.py
   ```

3. Follow the output instructions to serve the game in a browser.

## How to Play

- The ball moves at an initial angle, bouncing off paddles and walls.
- The game detects goals, restarts the ball, and updates the score.
- Players can control paddles smoothly with clamping to keep paddles within the screen.
- The screen updates in real time, maintaining a 60 FPS frame rate for smooth play.

## Game Controls

- `P` Key: Start the game and move the ball.
- `R` Key: Restart the game.
- Player 1 Controls:
  - `W` Key: Move paddle up.
  - `S` Key: Move paddle down.
- Player 2 Controls:
  - `UP` Arrow: Move paddle up.
  - `DOWN` Arrow: Move paddle down.

---

## Future Enhancements
- Add an AI competitor.
- Mobile-friendly version with touch controls.
- Add on-screen instructions.

---

### Author
*Tunde Adepitan*  
GitHub: [tunde262](https://github.com/tunde262)  
Feel free to connect and give me feedback!
