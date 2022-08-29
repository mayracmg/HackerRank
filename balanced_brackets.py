#!/bin/python3

import math
import os
import random
import re
import sys

def isBalanced(s):
    open_brackets = []

    for bracket in s:
        if (bracket == '{' or bracket == '(' or bracket == '['):
            open_brackets.append(bracket)
        else:
            try:
                last_bracket = open_brackets[-1]
                pair = last_bracket + bracket
                
                if (pair == '{}' or pair == '()' or pair == '[]'):
                    open_brackets.pop()
                else:
                    return "NO"
                    
            except:
                return "NO"
    if (len(open_brackets) == 0):
        return "YES"
    
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
