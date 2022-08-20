#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n = 26 
    encrypted_message = ''
    
    for letter in s:
        new_letter = letter
        
        for i in range(n):
            if (letter == lower_alphabet[i]):
                new_letter = lower_alphabet[(i + k) % n]
                break
            if (letter == upper_alphabet[i]):
                new_letter = upper_alphabet[(i + k) % n]
                break
        encrypted_message += new_letter
    return encrypted_message
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
