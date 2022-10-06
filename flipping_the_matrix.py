#!/bin/python3

import math
import os
import random
import re
import sys

def flippingMatrix(matrix):
    n_2 = len(matrix)
    middle = n_2 // 2
    n = n_2 - 1
    max_sum = 0
    
    for i in range(middle):
        for j in range(middle):
            temp = []
            temp.append(matrix[i][j])
            temp.append(matrix[i][n - j])
            temp.append(matrix[n - i][j])
            temp.append(matrix[n - i][n - j])
            
            max_sum += max(temp)
    return max_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
