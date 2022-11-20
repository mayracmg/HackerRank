#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def bomberMan(n, grid):
    rows = len(grid)
    cols = len(grid[0])
    
    for i in range(rows):
        grid[i] = [*grid[i]]

    previous_grid = ""
    second = 2
    
    while second <= n:
        if (second % 2 == 0):
            for i in range(rows):
                for j in range(cols):
                    if (grid[i][j] == '.'):
                        grid[i][j] = 'O'
                    else:
                        grid[i][j] = 'X'
                                   
        if (second % 2 == 1):
            for i in range(rows):
                for j in range(cols):
                    if (grid[i][j] == 'X'):
                        grid[i][j] = '.'
                        
                        if (i > 0 and grid[i - 1][j] == 'O'):
                            grid[i - 1][j] = '.'
                        if (i + 1 < rows and grid[i + 1][j] == 'O'):
                            grid[i + 1][j] = '.'

                        if (j > 0 and grid[i][j - 1] == 'O'):
                            grid[i][j - 1] = '.'
                        if (j + 1 < cols and grid[i][j + 1] == 'O'):
                            grid[i][j + 1] = '.'
        
        if (str(grid) == previous_grid):
            second = n - ((n - 1) % 4) 
            previous_grid = ""
                
        elif (second % 4 == 1):
            previous_grid = str(grid)
            
        second += 1

    for i in range(rows):
        grid[i] = ''.join(grid[i]).replace('X', 'O')

    return grid
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
