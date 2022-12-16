#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(h):
    max_area = 0
    stack = []
    # [start_position = 1, altura = 2]
    # [start_position = 2, altura = 3]
    
    for i, current_height in enumerate(h):
        start_position = i
        
        while stack and stack[-1][1] > current_height:
            index, height = stack.pop()
            current_area = (i - index) * height
            max_area = max(max_area, current_area)
            start_position = index
            
        stack.append((start_position, current_height))
        
    for i, current_height in stack:
        current_area = current_height * (len(h) - i)
        max_area = max(max_area, current_area)
        
    return max_area

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
