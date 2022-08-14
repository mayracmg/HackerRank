import math
import os
import random
import re
import sys

def countingSort(arr):
    counting = [0 for x in range(100)]

    for number in arr:
        counting[number] += 1
    
    return counting    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
