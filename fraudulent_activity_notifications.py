#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#
def find_median(last_expenses, d):
    i = d // 2
    median = last_expenses[i]
    if (d % 2 == 0):
        median += last_expenses[i - 1]
    else:
        median *= 2
    return median

def activityNotifications(expenditure, d):
    n = len(expenditure)
    notifications = 0    
    last_expenses = [] 
    for i in range(d):
        bisect.insort_left(last_expenses, expenditure[i])
    median = find_median(last_expenses, d)
    
    for i in range(d, n):
        spend = expenditure[i]
        if (spend >= median):
            notifications += 1
        
        k = bisect.bisect_left(last_expenses, expenditure[i - d])
 
        last_expenses.pop(k)
        bisect.insort_left(last_expenses, spend)
           
        median = find_median(last_expenses, d)
        
    return notifications

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
