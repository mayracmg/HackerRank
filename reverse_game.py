#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    t = int(input().strip())

    for _ in range(t):
        first_multiple_input = input().rstrip().split()
        
        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])
        
        balls = []
        i = 0
        
        for _ in range(n // 2):
            balls.append(n - 1 - i)
            balls.append(i)
            i += 1
        balls.append(i)
        print(balls.index(k))
