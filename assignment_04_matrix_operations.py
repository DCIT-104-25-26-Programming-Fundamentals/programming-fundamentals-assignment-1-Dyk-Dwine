# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def transposeMatrix(matrix, rows, cols):
    result = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    return result


def addMatrices(matrixA, matrixB, rows, cols):
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrixA[i][j] + matrixB[i][j]
    return result


def multiplyMatrices(matrixA, matrixB, rowsA, colsA, colsB):
    result = [[0 for _ in range(colsB)] for _ in range(rowsA)]
    for i in range(rowsA):
        for j in range(colsB):
            for k in range(colsA):
                result[i][j] += matrixA[i][k] * matrixB[k][j]
    return result


def readMatrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))
        matrix.append(row)
    return matrix


def printMatrix(matrix, rows, cols):
    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end=" ")
        print()


#Main block 
print("Matrix Operations Menu:")
print("1. Transpose a Matrix")
print("2. Add Two Matrices")
print("3. Multiply Two Matrices")
choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = readMatrix(rows, cols)
    transposed = transposeMatrix(matrix, rows, cols)

    print("Original Matrix:")
    printMatrix(matrix, rows, cols)
    print("Transposed Matrix:")
    printMatrix(transposed, cols, rows)

elif choice == 2:
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    print("Matrix A:")
    matrixA = readMatrix(rows, cols)
    print("Matrix B:")
    matrixB = readMatrix(rows, cols)

    summed = addMatrices(matrixA, matrixB, rows, cols)

    print("Matrix A:")
    printMatrix(matrixA, rows, cols)
    print("Matrix B:")
    printMatrix(matrixB, rows, cols)
    print("Sum of Matrices:")
    printMatrix(summed, rows, cols)

elif choice == 3:
    rowsA = int(input("Enter number of rows for Matrix A: "))
    colsA = int(input("Enter number of columns for Matrix A: "))
    print("Matrix A:")
    matrixA = readMatrix(rowsA, colsA)

    rowsB = colsA  # Number of rows in B must equal number of columns in A
    colsB = int(input("Enter number of columns for Matrix B: "))
    print("Matrix B:")
    matrixB = readMatrix(rowsB, colsB)

    product = multiplyMatrices(matrixA, matrixB, rowsA, colsA, colsB)

    print("Matrix A:")
    printMatrix(matrixA, rowsA, colsA)
    print("Matrix B:")
    printMatrix(matrixB, rowsB, colsB)
    print("Product of Matrices (A x B):")
    printMatrix(product, rowsA, colsB)