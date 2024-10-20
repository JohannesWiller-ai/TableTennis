# Table Tennis Score Tracker

A graphical score tracking application for table tennis matches, designed to resemble a traditional manual scoreboard. This application provides an intuitive interface for keeping track of scores during a game, using simple keyboard inputs to add points, undo actions, reset the game, and quit the application.

---

## Table of Contents

- [Table Tennis Score Tracker](#table-tennis-score-tracker)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Installation](#installation)
    - [1. Clone the Repository](#1-clone-the-repository)
    - [2. Create a Virtual Environment](#2-create-a-virtual-environment)
    - [3. Activate the Virtual Environment](#3-activate-the-virtual-environment)
    - [4. Install Dependencies](#4-install-dependencies)
  - [Usage](#usage)
    - [1. Run the Application](#1-run-the-application)
    - [2. Gameplay Controls](#2-gameplay-controls)
    - [3. Winner Detection](#3-winner-detection)
  - [Project Structure](#project-structure)
  - [Screenshots](#screenshots)
  - [License](#license)
  - [Credits](#credits)
  - [Contributing](#contributing)
  - [Support](#support)
  - [Acknowledgments](#acknowledgments)

---

## Features

- **Traditional Aesthetic**: Mimics the look of old-school flip scoreboards used in table tennis and badminton.
- **Keyboard Controls**:
  - Press `1` to add a point to **Claiminizzer 1**.
  - Press `2` to add a point to **Claiminizzer 2**.
  - Press `u` to undo the last action.
  - Press `r` to reset the game.
  - Press `q` to exit the application.
- **Automatic Winner Detection**: Inverts the colors of the winner's scorecard when the winning conditions are met.
- **Responsive Design**: Starts in fullscreen mode, and the score display adjusts according to the screen size.

---

## Requirements

- **Python 3.x**
- **tkinter** (usually included with Python)

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/TableTennis.git
cd TableTennis
```

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

```bash
# For Unix/Linux
python3 -m venv venv

# For Windows
python -m venv venv
```

### 3. Activate the Virtual Environment

```bash
# For Unix/Linux
source venv/bin/activate

# For Windows
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

> **Note**: The `requirements.txt` is empty because no external packages are required beyond the standard library. If `tkinter` is not installed, you may need to install it separately.

- **For Debian/Ubuntu**

  ```bash
  sudo apt-get install python3-tk
  ```

- **For macOS**

  `tkinter` is usually included with Python on macOS. If not, you might need to install it via Homebrew:

  ```bash
  brew install python-tk
  ```

- **For Windows**

  `tkinter` is included with the standard Python installer for Windows.

---

## Usage

### 1. Run the Application

Make sure your virtual environment is activated.

```bash
python main.py
```

> **Note**: Use `python3` instead of `python` if necessary.

### 2. Gameplay Controls

- **Adding Points**
  - Press `1` to add a point to **Claiminizzer 1**.
  - Press `2` to add a point to **Claiminizzer 2**.
- **Undo Last Action**
  - Press `u` to undo the last action.
- **Reset Game**
  - Press `r` to reset the game.
- **Exit Application**
  - Press `q` to exit the application.

### 3. Winner Detection

- When a player reaches 11 points with at least a 2-point lead, their scorecard's colors will be inverted, indicating they have won the game.
- If you undo points and the winning conditions are no longer met, the color inversion will be removed, and the game continues.

---

## Project Structure

- `main.py`: The main script that runs the GUI application.
- `classes.py`: Contains the `Game` class that manages the game logic.
- `requirements.txt`: Lists the project dependencies (if any).

---

## Screenshots

*(Include screenshots of the application here to give users a visual preview.)*

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Credits

Developed by **Your Name**.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Commit your changes:

   ```bash
   git commit -am 'Add a new feature'
   ```

4. Push to the branch:

   ```bash
   git push origin feature/your-feature-name
   ```

5. Open a Pull Request.

---

## Support

If you have any questions or need assistance, feel free to open an issue or contact me directly.

---

## Acknowledgments

- Thanks to all contributors and users who have helped improve this project.

---

**Enjoy your game!**