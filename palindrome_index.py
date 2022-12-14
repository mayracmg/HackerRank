#!/bin/python3

import math
import os
import random
import re
import sys

def palindromeIndex(s):
    n = len(s)
    reversed_s = s[::-1]
    
    if (s == reversed_s):
        return -1
    
    for i in range(n):
        new_s = s[:i] + s[i + 1:]
        new_reversed_s = reversed_s[:n - i - 1] + reversed_s[n - i:]
        if (new_s == new_reversed_s):
            return i
            
    return -1
           
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
