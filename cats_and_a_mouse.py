#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    cat_A_position = x
    cat_B_position  = y
    mouse_C_position  = z
    
    distance_between_A_C = abs(cat_A_position - mouse_C_position)
    distance_between_B_C = abs(cat_B_position - mouse_C_position)
    
    if (distance_between_A_C < distance_between_B_C):
        return "Cat A"
    elif (distance_between_B_C < distance_between_A_C):
        return "Cat B"
    return "Mouse C"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
