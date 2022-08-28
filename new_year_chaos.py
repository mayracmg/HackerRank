import math
import os
import random
import re
import sys

def minimumBribes(q):
    n = len(q)
    ideal_q = [i for i in range(1, n + 1)]
    bribes = 0
    
    while (q != ideal_q):
        for i in range(n):
            sequence_position = i + 1
            moves = q[i] - sequence_position
            
            if (moves > 2):
                print("Too chaotic")
                return
            
            if (q[i] != sequence_position):
                if (q[i] > q[i + 1]):
                    q[i], q[i + 1] = q[i + 1], q[i]
                    bribes += 1
    print(bribes)  

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
