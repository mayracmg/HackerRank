import math
import os
import random
import re
import sys


def timeConversion(s):
   
    am_pm = s[-2:]
    time = s[:-2].split(":")
    hours = int(time[0])
    minutes = time[1]
    seconds = time[2]
        
    if (am_pm == 'PM'):
        hours = hours + 12

    if (hours % 12 == 0):
        hours -= 12
            
    military_time = str(hours).zfill(2) + ":" + minutes + ":" + seconds

    return military_time

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
