import math
import os
import random
import re
import sys

def plusMinus(arr):
    total_numbers = 0
    positives = 0
    negatives = 0
    zeros = 0
    
    for number in arr:
        total_numbers += 1
        if (number < 0):
            negatives += 1
        elif (number > 0):
            positives += 1
        else:
            zeros += 1

    positive_ratio = round(positives / total_numbers, 6)
    negative_ratio = round(negatives / total_numbers, 6)
    zero_ratio = round(zeros / total_numbers, 6)
    
    print(positive_ratio)
    print(negative_ratio)
    print(zero_ratio)
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
