#!/bin/python3

import math
import os
import random
import re
import sys

def breakingRecords(scores):
    worst_record_count = 0
    best_record_count = 0
    
    min_record = scores[0]
    max_record = scores[0]
    
    for s in scores:
        if s > max_record:
            best_record_count += 1
            max_record = s
            
        if s < min_record:
            worst_record_count += 1
            min_record = s
    
    return [best_record_count, worst_record_count]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
