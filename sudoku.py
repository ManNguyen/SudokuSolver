
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
                return False

        return True

def possibleVal(row,cArr):
        nPSet= []
        for i in cArr:
            if i not in row : nPSet.append(i)
        return nPSet

def cloneGrid(grid):
        r =[]
        for row in grid:
            nRow = [c for c in row]
            r.append(nRow)
        return r

cNumSet = [1, 2, 3, 4, 5, 6, 7, 8, 9]
class Sudoku:

    def __init__(self, grid):
        self.grid = grid
        self.origin = cloneGrid(grid)

    def isValid(self) -> bool:
        grid = self.grid
        if(len(grid) != 9):
            print("invalid number of rows")
            return False
        for row in grid:
            if(len(row) != 9):
                print("invalid number of cols")
                print("\"", row, "\"")
                return False

        for row in grid:
            if(checkUnique(row) == False):
                return False

        for row in rotateGrid(grid):
            if(checkUnique(row) == False):
                return False

        for row in unboxGrid(grid):
            if(checkUnique(row) == False):
                return False
        return True


    def printOrigin(self):
        grid =  self.origin
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

    def print(self):
        grid = self.grid
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

    def solve(self):
        # self.print()
        # print()
        grid = self.grid
        rGrid = rotateGrid(grid)
        uGrid = unboxGrid(grid)

        testX,testY =0,0
        cand = []

    # GREEDY PART: check for impossible cases and check for easy to solve cells
        for y, row in enumerate(grid):
            secY = (y//3)
            for x, cell in enumerate(row):
                if cell == 0:

                    # Find possible values based on Row Check
                    candidates = possibleVal(grid[y],cNumSet)

                    # Filter possible values based on Column Check
                    candidates = possibleVal(rGrid[x],candidates)

                    secX = (x//3)
                    boxIndex = secX+3*secY

                    # Filter possible values based on Box Check
                    candidates = possibleVal(uGrid[boxIndex],candidates)
    
                    if len(candidates) == 0: return False
                    if len(candidates) == 1:
                        # IF there is one possible value then be it
                        self.grid[y][x] = candidates[0]
                        return self.solve()

                    # Just keep track of one unsolved cell is enough
                    testX,testY =x,y
                    cand = candidates
             
        if(self.isValid()):
            return True

        # Cache the current Sudoku
        tempGrid = cloneGrid(self.grid) 

        # BACKTRACKING
        for val in cand:
            self.grid[testY][testX] = val
            res = self.solve()

            if(res): return True
            else: self.grid = cloneGrid(tempGrid)

        return False
