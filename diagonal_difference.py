import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    left_diagonal = 0
    right_diagonal = 0
    n = len(arr)
    
    for i in range(n):
        left_diagonal += arr[i][i]
        right_diagonal += arr[i][n - i - 1]
    
    difference = abs(right_diagonal - left_diagonal)
    
    return difference
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
