import math
import os
import random
import re
import sys

def superDigit(n, k):
    if (len(n) == 1):
        return n
    
    super_digit = n
    while (len(super_digit) > 1):
        sum_digits = 0
        
        for digit in super_digit:
            sum_digits += int(digit)
            
        if (super_digit == n):
            sum_digits *= k
            
        super_digit = str(sum_digits)
        
    return int(super_digit)
  
def superDigit_Recursive(n, k):
    if (len(n) == 1):
        return int(n)
    else:
        sum_digits = 0
        for digit in n:
            sum_digits += int(digit)
        super_digit = str(sum_digits * k)

        return superDigit(super_digit, 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
