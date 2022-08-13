import math
import os
import random
import re
import sys

def lonelyinteger(a):
    count_numbers = {}
    lonely_integer = 0
    
    for number in a:
        try:
            count_numbers[number] = count_numbers[number] + 1
        except:
            count_numbers[number] = 1

    for key in count_numbers:
        if count_numbers[key] == 1:
            lonely_integer = key
    
    return lonely_integer
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
