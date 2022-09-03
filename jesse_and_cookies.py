#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

def cookies(k, A):
    operations = 0
    #A.sort()
    heapq.heapify(A)
    
    while True:
        cookie_1 = heapq.heappop(A) #A.pop(0)
        
        if (cookie_1 >= k):
            return operations
        if A:
            cookie_2 = heapq.heappop(A) #A.pop(0)
            new_cookie = cookie_1 + (2 * cookie_2)
            
            heapq.heappush(A, new_cookie)
            #A.append(new_cookie)
            #A.sort()
            operations += 1
        else:
            return -1        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
