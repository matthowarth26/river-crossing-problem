# Farmer–Lion–Goat–Grass (BFS & DFS)

A clean, testable implementation of the classic river-crossing puzzle using **Breadth-First Search (BFS)** and
**Depth-First Search (DFS)**.

## Puzzle rules

You must move all entities from the **left** bank to the **right** bank.

- The **farmer** can cross the river alone or with **one passenger** (lion, goat, or grass).
- If the **lion** is left alone with the **goat** *without the farmer*, the goat gets eaten.
- If the **goat** is left alone with the **grass** *without the farmer*, the grass gets eaten.

A state is represented by which side (L/R) each entity is on: `F, L, G, Gr`.

## Run

```bash
# BFS (shortest solution)
python main.py --method bfs --show-states

# DFS (stack-based)
python main.py --method dfs --show-states
```

## Why BFS vs DFS?

- **BFS** explores by layers, so the first time it reaches the goal it has found the **minimum number of moves**.
- **DFS** goes deep first; it may find a solution quickly, but it is **not guaranteed** to be shortest.

## Tests

```bash
pytest -q
```

The test suite verifies:
- rule correctness (invalid states rejected)
- successor generation (legal moves only)
- BFS produces a valid, **shortest** solution
- DFS produces a valid solution
