# SudokuSolver

## Description

This repo is created to solve a 9x9 sudoku problem using Python

## Getting Started

The Sudoku class will take in the [9][9] array as unsolved Sudoku

The unsolved cells need to be coded as 0

```{python}
grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]
sudoku = Sudoku(grid)
```

function solve will try to solve it. And if it's solvable, the functio return True

You can then extract the solved grid in property grid. You can also get the original(unsolved grid) in property origin. There're also function print and printOrigin to print the sudoku out nicely :)

```{python}

solvable = sudoku.solve()

if(solvable):
        print("grid solved")
        sudoku.printOrigin()
        sudoku.print()
print(sudoku.grid)
print(sudoku.origin)
```





### Executing program

* How to run the program
* Step-by-step bullets
```
code blocks for commands
```
