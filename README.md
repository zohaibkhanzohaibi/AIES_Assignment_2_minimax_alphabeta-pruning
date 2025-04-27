# Tic Tac Toe AI - Minimax and Alpha-Beta Pruning
Welcome to the Tic Tac Toe AI project!
This repository contains two Python implementations of Tic Tac Toe where an AI plays against a human using:

Basic Minimax Algorithm

Minimax with Alpha-Beta Pruning

Both versions are compared in terms of efficiency by counting the number of minimax checks (evaluations) during gameplay.

# Key Differences

| Feature                 | Minimax Only                      | Alpha-Beta Pruning                       |
|--------------------------|-----------------------------------|------------------------------------------|
| **Speed**                | Slower for complex trees          | Faster by skipping unnecessary branches  |
| **Number of Evaluations**| High                              | Significantly lower                      |
| **Code Complexity**      | Simple recursion                  | Slightly more complex with pruning logic |
| **Optimal Play**         | ✅ Always finds best move         | ✅ Always finds best move                 |

✅ Both algorithms always play perfectly.

♻️ Alpha-Beta just does it faster by avoiding redundant calculations!

## How to Run

1. **Clone the repository** or **download** the files.

2. **Run either script using Python 3**:

```bash
python tic_tac_toe_minimax.py
```

or
```bash
python tic_tac_toe_alpha_beta.py
```

## Gameplay Instructions
The human always plays first (O).

Enter your move by typing two numbers (row and column) separated by a space.
Example:

```bash
0 2
```
(Top row, third column)

## After each AI move:
The number of evaluations (checks) made by the AI will be printed on the screen.

## At the end of the game:
The total number of evaluations during the entire game will be displayed.



