#!/bin/python3

import math
import os
import random
import re
import sys
#import statistics

def findMedian(arr):
    n = len(arr)
    arr.sort()
    
    i = n // 2
    median = arr[i]
    
    return median

    #return statistics.median(arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
