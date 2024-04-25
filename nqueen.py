import numpy as np

n = int(input("Enter the size of the matrix"))
matrix = np.zeros([n, n])

def checckboard(r, c):
    if r == n:
        return True  
    for col in range(n):
        if issafe(r, col):
            matrix[r][col] = 1
            if checckboard(r + 1, c):  
                return True
            matrix[r][col] = 0  
    return False

def columnsafe(row, col):
    for i in range(row):
        if matrix[i][col] == 1:
            return False
    return True

def isrightdiagonal(row, col):
    i, j = row, col
    while i >= 0 and j >= 0:
        if matrix[i][j] == 1:
            return False
        i -= 1
        j -= 1
    return True

def isleftdiagonal(row, col):
    i, j = row, col
    while i >= 0 and j < n:
        if matrix[i][j] == 1:
            return False
        i -= 1
        j += 1
    return True

def issafe(row, col):
    return columnsafe(row, col) and isleftdiagonal(row, col) and isrightdiagonal(row, col)

if checckboard(0, 0):
    print("Solution exists. The chessboard with queens placed is:")
    print(matrix)
else:
    print("No solution exists.")

