#!/usr/bin/env python3

# LU decomposition from A matrix to L and U

import numpy as np
import time

def printLU(a, l, u):
    print("A matrix: ")
    print(a)
    print("L matrix: ")
    print(np.matrix(l))
    print("U matrix: ")
    print(np.matrix(u))

def printDuration(start, end):
    print("\nTime of execution (seconds): %0.10f" %(end - start))

def luDecomposition(matrix, n):
    upper = np.zeros((n,n), dtype=float)
    lower = np.zeros((n,n), dtype=float)
    start = time.time()

    for i in range(n):
        # U matrix
        for k in range(i, n):
            sum = 0
            for j in range(i):
                sum += (lower[i][j] * upper[j][k])
            upper[i][k] = matrix[i][k] - sum
        
        # L matrix    
        for k in range(i, n):
            if i == k:
                lower[i][i] = 1
            else:   
                sum = 0
                for j in range(i):
                    sum += (lower[k][j] * upper[j][i])
                lower[k][i] = ((matrix[k][i] - sum) / upper[i][i])
    end = time.time()
    printLU(matrix, lower, upper)
    printDuration(start, end)
    

SIZE = 3
random_matrix = np.random.randint(10, size=(SIZE,SIZE))
matrix = [[4,3],[6,3]]
matrix2 = [[1,3,-2],[4,2,8],[-3,1,0]]

luDecomposition(matrix2, SIZE)