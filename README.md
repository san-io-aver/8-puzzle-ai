# 8-Puzzle Solver: An AI Exploration

A fully interactive 8-Puzzle game built with Python and Tkinter, designed to demonstrate search algorithms and state-space logic. This project serves as a foundation for implementing **Heuristic-based Search (A-Star)** and **Breadth-First Search (BFS)**.

---

## Features

- **Interactive GUI:** A responsive 3x3 grid built with `Tkinter` that handles real-time user input.
- **Smart Scramble Engine:** Utilizes **Inversion Count Parity** to ensure that every generated puzzle is mathematically solvable.
- **State Management:** Includes "Reset to Initial" functionality to allow for debugging and re-playing specific board configurations.
- **OOP Architecture:** Clean, class-based structure separating game logic (Environment) from the UI (View).

---

## The Logic Behind the Game

### 1. Solvability Engine
Not every random arrangement of an 8-puzzle can be solved. This project implements a mathematical check based on **Inversions**. 
* An inversion is a pair of tiles (a, b) such that a > b but a appears before b.
* **Theorem:** An 8-puzzle state is solvable if and only if the number of inversions is **even**.
* The `scramble()` method continuously shuffles until an even-parity state is found.

### 2. State Mapping
The board is represented as a 1D list `[1, 2, 3, 4, 5, 6, 7, 8, 0]` but processed using 2D coordinate geometry:
- **Row:** `index // 3`
- **Column:** `index % 3`

---

## Installation & Usage

1. **Clone the repository:**
    https://github.com/san-io-aver/8-puzzle-ai.git

2. **Run the application:**
    python main.py

---
## Roadmap (Next Steps)

- [ ] **Heuristic Implementation:** Add Manhattan Distance and Hamming Distance calculations.
- [ ] **AI Solver:** Implement the **A-Star Search Algorithm** to find the optimal path to the goal.
- [ ] **Visualization:** Animate the AI's solution steps using `self.root.after()`.

---

## 🎓 Academic Context
Developed as part of an **AI/ML Coursework** to explore state-space search complexity O(b^d) and the importance of informed heuristics in reducing the effective branching factor.