


testGrid2 = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
             [6, 7, 2, 1, 9, 5, 3, 4, 8],
             [1, 9, 8, 3, 4, 2, 5, 6, 7],
             [8, 5, 9, 7, 6, 1, 4, 2, 3],
             [4, 2, 6, 8, 5, 3, 7, 9, 1],
             [7, 1, 3, 9, 2, 4, 8, 5, 6],
             [9, 6, 1, 5, 3, 7, 2, 8, 4],
             [2, 8, 7, 4, 1, 9, 6, 3, 5],
             [3, 4, 5, 2, 8, 6, 1, 7, 9]]






def checkUnique(row) ->bool:
    numSet = set([])

    for num in row:
        if num in numSet:
            print("repeated values")
            print("\"",row,"\"")
            return False
        numSet.add(num)

    for i in range(1,10):
        if i not in numSet:
            print("missing value")
            print("\"",row,"\"")
            print(i)


def isValid(grid) ->bool:

    if(len(grid) != 9) :
        print("invalid number of rows")
        return False

    for row in grid:
        if(len(row) != 9) :
            print("invalid number of cols")
            print("\"",row,"\"")
            return False



    print("checking rows...")
    for row in grid:
      if(checkUnique(row) == False): return False

    print("checking cols...")
    for row in rotateGrid(grid):
      if(checkUnique(row) == False): return False

    print("checking sections...")
    for row in unboxGrid(grid):
      if(checkUnique(row) == False): return False


    return True

def rotateGrid(grid):
    rGrid = []
    for i in range(9):
        rGrid.append([x[i] for  x in grid])
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
            rowIndex= secX+3*secY
            rGrid[rowIndex].append(cell)
    return rGrid


def printSudoku(grid):
    vline = '_______________________________'
    print(vline)
    for idx, row in enumerate(grid):
        print("|",end = '')
        for idy, cell in enumerate(row):
            if cell != 0: print('',cell,'',end = '')
            else: print('   ',end = '')
            if idy%3 == 2:  print("|",end = '')
        print("")
        if idx%3 == 2:  print(vline)


# printSudoku(testGrid2)
# printSudoku(rotateGrid(testGrid2))
# printSudoku(unboxGrid(testGrid2))



print(isValid(solvedgrid))


