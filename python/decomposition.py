#!/usr/bin/env python3

# LU decomposition from A matrix to L and U

import numpy as np
import time
import pymp
import multiprocessing

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
    upper = pymp.shared.array((n,n), dtype=float)
    lower = pymp.shared.array((n,n), dtype=float)
    for i in range(0, n):
        for j in range(0, n):
            upper[i][j] = 0.0
            lower[i][j] = 0.0
    
    start = time.time()
    
    with pymp.Parallel(multiprocessing.cpu_count()) as p:
        for i in p.xrange(n):
            # U matrix
            for k in range(i, n):
                sum = 0.0
                for j in range(i):
                    sum += (lower[i][j] * upper[j][k])
                upper[i][k] = matrix[i][k] - sum
                
            # L matrix 
            for k in range(i, n):
                if i == k:
                    lower[i][i] = 1
                else:   
                    sum = 0.0
                    for j in range(i):
                        sum += (lower[k][j] * upper[j][i])
                    lower[k][i] = ((matrix[k][i] - sum) / upper[i][i])
    end = time.time()
    #printLU(matrix, lower, upper)
    printDuration(start, end)
    

SIZE = 1000
random_matrix = np.random.randint(10, size=(SIZE,SIZE))
matrix = [[4,3],[6,3]]
matrix2 = [[1,3,-2],[4,2,8],[-3,1,0]]

luDecomposition(random_matrix, SIZE)