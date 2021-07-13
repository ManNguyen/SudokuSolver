

solveGrid = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
             [6, 7, 2, 1, 9, 5, 3, 4, 8],
             [1, 9, 8, 3, 4, 2, 5, 6, 7],
             [8, 5, 9, 7, 6, 1, 4, 2, 3],
             [4, 2, 6, 8, 5, 3, 7, 9, 1],
             [7, 1, 3, 9, 2, 4, 8, 5, 6],
             [9, 6, 1, 5, 3, 7, 2, 8, 4],
             [2, 8, 7, 4, 1, 9, 6, 3, 5],
             [3, 4, 5, 2, 8, 6, 1, 7, 9]]


testGrid = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
             [6, 0, 2, 1, 9, 5, 3, 4, 8],
             [1, 9, 8, 3, 4, 2, 5, 0, 7],
             [8, 5, 9, 7, 6, 1, 4, 2, 3],
             [4, 2, 6, 0, 5, 3, 7, 9, 1],
             [7, 1, 3, 9, 2, 4, 8, 5, 6],
             [9, 6, 1, 5, 3, 7, 2, 8, 4],
             [2, 8, 7, 4, 1, 9, 6, 0, 5],
             [3, 4, 5, 2, 8, 6, 1, 0, 9]]

grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]




cNumSet = [1, 2, 3, 4, 5, 6, 7, 8,9]

def cloneGrid(grid):
    r =[]
    for row in grid:
        nRow = [c for c in row]
        r.append(nRow)
    return r


def checkUnique(row) -> bool:
    numSet = set([])

    for num in row:
        if num in numSet:
            # print("repeated values")
            # print("\"", row, "\"")
            return False
        numSet.add(num)

    for i in range(1, 10):
        if i not in numSet:
            # print("missing value")
            # print("\"", row, "\"")
            # print(i)
            return False

    return True


def isValid(grid) -> bool:

    if(len(grid) != 9):
        print("invalid number of rows")
        return False

    for row in grid:
        if(len(row) != 9):
            print("invalid number of cols")
            print("\"", row, "\"")
            return False

    # print("checking rows...")
    for row in grid:
      if(checkUnique(row) == False):
          return False

    # print("checking cols...")
    for row in rotateGrid(grid):
      if(checkUnique(row) == False):
          return False

    # print("checking sections...")
    for row in unboxGrid(grid):
      if(checkUnique(row) == False):
          return False

    return True


def rotateGrid(grid):
    rGrid = []
    for i in range(9):
        rGrid.append([x[i] for x in grid])
    return rGrid

def unboxGrid(grid):
    rGrid = [
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        []
    ]
    for idy, row in enumerate(grid):
        secY = (idy//3)
        for idx, cell in enumerate(row):
            secX = (idx//3)
            rowIndex = secX+3*secY
            rGrid[rowIndex].append(cell)
    return rGrid

def printSudoku(grid):
    vline = '_______________________________'
    print(vline)
    for idx, row in enumerate(grid):
        print("|", end='')
        for idy, cell in enumerate(row):
            if cell != 0:
                print('', cell, '', end='')
            else:
                print('   ', end='')
            if idy % 3 == 2:
                print("|", end='')
        print("")
        if idx % 3 == 2:
            print(vline)


def possibleVal(row,cArr):
    nPSet= []
    for i in cArr:
        if i not in row : nPSet.append(i)
    return nPSet

def solveGrid(grid):

    rGrid = rotateGrid(grid)
    uGrid = unboxGrid(grid)

    for y, row in enumerate(grid):
      secY = (y//3)
      for x, cell in enumerate(row):
        if cell == 0:
            candidates = possibleVal(grid[y],cNumSet)
            candidates = possibleVal(rGrid[x],candidates)
            secX = (x//3)
            boxndex = secX+3*secY
            candidates = possibleVal(uGrid[boxndex],candidates)
            if len(candidates) == 0: return False

            cGrid = cloneGrid(grid)

            for c in candidates:
                cGrid[y][x] = c
                printSudoku(cGrid)
                print()
                if(isValid(cGrid)) : return cGrid
                next = solveGrid(cGrid)

                if(next) :return next

    return False


# printSudoku(testGrid2)
# printSudoku(rotateGrid(testGrid2))
# printSudoku(unboxGrid(testGrid2))

printSudoku(grid)
cGrid = solveGrid(grid)
printSudoku(cGrid)

printSudoku(testGrid)
cGrid = solveGrid(testGrid)
printSudoku(cGrid)
