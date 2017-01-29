import copy
import sys

if len(sys.argv) < 2:
    iterations = 1
    SIZE = 10
else:
    iterations = int(sys.argv[1])
    SIZE = int(iterations*iterations*2)

matrix = [[[0, 0, 0, 0]] * SIZE * 2 for i in range(SIZE)]
drawMatrix = [[0] * SIZE * 2 for i in range(SIZE)]

startX = newPivotX = int(SIZE / 3)
startY = newPivotY = int(SIZE / 2)
startDir = 0
matrix[startX][startY] = [1, 0, 0, 0]

print(f"Generating dragon curve of {iterations} iterations...")

for i in range(iterations):
    tempMatrix = copy.deepcopy(matrix)
    pivotX = newPivotX
    pivotY = newPivotY
    for x in range(SIZE):
        for y in range(SIZE * 2):

            diffX = pivotX - x
            diffY = y - pivotY

            xPos = pivotX + diffY
            yPos = pivotY + diffX

            if x == startX and y == startY:
                if startDir == 0:
                    newPivotX = xPos
                    newPivotY = yPos + 1
                if startDir == 1:
                    newPivotX = xPos + 1
                    newPivotY = yPos
                if startDir == 2:
                    newPivotX = xPos
                    newPivotY = yPos - 1
                if startDir == 3:
                    newPivotX = xPos - 1
                    newPivotY = yPos

            if matrix[x][y][0] == 1:
                tempMatrix[xPos][yPos] = [tempMatrix[xPos][yPos][0],
                                          1,
                                          tempMatrix[xPos][yPos][2],
                                          tempMatrix[xPos][yPos][3]]

            if matrix[x][y][1] == 1:
                tempMatrix[xPos][yPos] = [tempMatrix[xPos][yPos][0],
                                          tempMatrix[xPos][yPos][1],
                                          1,
                                          tempMatrix[xPos][yPos][3]]
            if matrix[x][y][2] == 1:
                tempMatrix[xPos][yPos] = [tempMatrix[xPos][yPos][0],
                                          tempMatrix[xPos][yPos][1],
                                          tempMatrix[xPos][yPos][2],
                                          1]
            if matrix[x][y][3] == 1:
                tempMatrix[xPos][yPos] = [1,
                                          tempMatrix[xPos][yPos][1],
                                          tempMatrix[xPos][yPos][2],
                                          tempMatrix[xPos][yPos][3]]
    matrix = copy.deepcopy(tempMatrix)

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j][0] == 1:
            try:
                drawMatrix[i][j * 2] = 1
            except:
                IndexError
        if matrix[i][j][1] == 1:
            try:
                drawMatrix[i][j * 2 + 1] = 2
            except:
                IndexError
        if matrix[i][j][2] == 1:
            try:
                drawMatrix[i + 1][j * 2] = 1
            except:
                IndexError
        if matrix[i][j][3] == 1:
            try:
                drawMatrix[i][j * 2 - 1] = 2
            except:
                IndexError

print("Writing to file...")
fo = open("dragon_curve.txt", "w")

for i in range(SIZE):
    string = ""
    for j in range(SIZE * 2):
        if drawMatrix[i][j] == 0:
            string += " "
        elif drawMatrix[i][j] == 1:
            string += "|"
        else:
            string += "_"

    if string.__contains__("|") or string.__contains__("_"):
        fo.write(string + "\n")

fo.close()

print("Done! Dragon curve drawn in text file 'dragon_curve.txt'")
