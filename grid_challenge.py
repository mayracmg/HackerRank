import math
import os
import random
import re
import sys

def gridChallenge(grid):
    n = len(grid)
    sorted_grid = []
    
    for i in range(n):
        current_row = sorted(grid[i])
        if (len(current_row) < n ):
            current_row = str(current_row).ljust(n, ' ')
        sorted_grid.append(current_row)
    
    for i in range(1, n):
        for j in range(n):
            if (sorted_grid[i][j] < sorted_grid[i - 1][j]):
                return "NO"

    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
