SIZE = 8
matrix = [[[0]*4]*SIZE*3*2 for i in range(SIZE*2)]
drawMatrix = [[0]*SIZE*3*2 for i in range(SIZE*2)]

'''
     |
0 =  .

1 =  ._

2 =  .
     |
3 = _.

 '''

startX = 2
startY = 2
matrix[startX][startY] = [1, 0, 0, 0]

def rotate(val):
    val += 1
    if val > 3:
        val = 0
    return val

for i in range(0):
    tempMatrix = [[0] * SIZE * 3 * 2 for i in range(SIZE * 2)]
    for a in range(len(matrix)):
        for b in range(len(matrix[0])):
            tempMatrix[a][b] = matrix[a][b]

    for x in range(SIZE):
        for y in range(SIZE*3):
            diffX = x - startX
            diffY = y - startY
            if matrix[x][y][0] == 1:
                tempMatrix[x + diffY][y + diffX][1] = 1
            elif matrix[x][y][1] == 1:
                tempMatrix[x + diffY][y + diffX][1] = 1
            elif matrix[x][y][2] == 1:
                tempMatrix[x + diffY][y + diffX][1] = 1
            elif matrix[x][y][3] == 1:
                tempMatrix[x + diffY][y + diffX][1] = 1

    matrix = tempMatrix.copy()

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j][0] == 1:
            drawMatrix[i][j] = 1
        if matrix[i][j][1] == 1:
            drawMatrix[i][j+1] = 2
        if matrix[i][j][2] == 1:
            drawMatrix[i+1][j] = 1
        if matrix[i][j][3] == 1:
            drawMatrix[i][j-1] = 2


for i in range(SIZE):
    string = ""
    for j in range(SIZE*3):
        if drawMatrix[i][j] == 0:
            string += " "
        elif drawMatrix[i][j] == 1:
            string += "|"
        else:
            string += "_"
    print(string)