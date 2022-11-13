#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'larrysArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY A as parameter.
#

def larrysArray(A):
    n = len(A)
    ideal_A = [i for i in range(1, n + 1)]
    
    for number_to_search in range(1, n - 1):
        current_position = A.index(number_to_search)
        
        if (number_to_search != current_position + 1):
            A.pop(current_position)
            mod = ((current_position + 1) - number_to_search) % 2

            if (mod == 0):
                i = number_to_search - 1
                A.insert(i, number_to_search)
            else:
                i = number_to_search
                A.insert(i, number_to_search)
                a = A[i - 1]
                b = A[i]
                c = A[i + 1]
                A[i - 1], A[i], A[i + 1] = b, c, a

    if (str(A) == str(ideal_A)):
        return 'YES'

    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
