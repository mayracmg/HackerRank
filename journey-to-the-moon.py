#!/bin/python3

import os
import queue

def journeyToMoon(n, astronaut):
    astronauts_left = len(astronaut)
    combinations = (n * (n - 1)) / 2
    
    q = queue.Queue()

    while astronauts_left > 0 or not q.empty():
        a = astronaut.pop()
        astronauts_left -= 1
        q.put(a[0])
        q.put(a[1])
      
        siblings = set()
        while not q.empty():
            start = q.get()
            siblings.add(start)
            for a in astronaut:
                if start in a:
                    q.put(a[0])
                    q.put(a[1])
                    
                    astronaut.remove(a)
                    astronauts_left -= 1

        siblings_n = len(siblings)
        combinations -= (siblings_n * (siblings_n - 1)) / 2

    return int(combinations)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    p = int(first_multiple_input[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()
