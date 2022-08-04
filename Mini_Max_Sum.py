import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    total_sum = 0
    max_number = 0
    min_number = 0
    
    for number in arr:
        total_sum += number
        
        if (number > max_number):
            max_number = number
        
        if (number < min_number or min_number == 0):
            min_number = number
        
    max_sum = total_sum - min_number
    min_sum = total_sum - max_number
    
    print(min_sum, max_sum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
