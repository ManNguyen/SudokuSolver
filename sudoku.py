
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
        print("check unique")
        print(row)
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



def isValid(grid) -> bool:
        if(len(grid) != 9):
            print("invalid number of rows")
            return False

        for row in grid:
            if(len(row) != 9):
                print("invalid number of cols")
                print("\"", row, "\"")
                return False

        print("checking rows...")
        for row in grid:
            if(checkUnique(row) == False):
                return False

        print("checking cols...")
        for row in rotateGrid(grid):
            if(checkUnique(row) == False):
                return False

        print("checking sections...")
        for row in unboxGrid(grid):
            if(checkUnique(row) == False):
                return False

        return True
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

        print("checking rows...")
        for row in grid:
            if(checkUnique(row) == False):
                return False

        print("checking cols...")
        for row in rotateGrid(grid):
            if(checkUnique(row) == False):
                return False

        print("checking sections...")
        for row in unboxGrid(grid):
            if(checkUnique(row) == False):
                return False
        return True


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
        self.print()
        grid = self.grid
        rGrid = rotateGrid(grid)
        uGrid = unboxGrid(grid)
        loopTime = None

        for y, row in enumerate(grid):
            secY = (y//3)
            for x, cell in enumerate(row):
                if cell == 0:
                    candidates = possibleVal(grid[y],cNumSet)
                    candidates = possibleVal(rGrid[x],candidates)
                    secX = (x//3)
                    boxIndex = secX+3*secY
                    candidates = possibleVal(uGrid[boxIndex],candidates)
                    if len(candidates) == 0: return False
                    print("for x =",x,"y=",y,"candidates is",candidates)
                    if len(candidates) == 1: 
                        self.grid[y][x] = candidates[0]
                        return self.solve()

                    
                    loopTime = len(candidates) if loopTime == None else loopTime * len(candidates)

        print("loop time:",loopTime)
        return False


# printSudoku(testGrid2)
# printSudoku(rotateGrid(testGrid2))
# printSudoku(unboxGrid(testGrid2))
