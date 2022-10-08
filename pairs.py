#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pairs(k, arr):
    arr.sort()
    n = len(arr)
    count = 0
    last_j = 0
    
    for i in range(n):
        for j in range(last_j + 1, n):
            diff = arr[j] - arr[i]
            
            if (diff == k):
                count += 1
                last_j = j
            
            if (diff >= k):
                break
            
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
