#!/bin/python3

import math
import os
import random
import re
import sys
import queue

def transform_object(nodes, s):
    distances = []
    for key, node in nodes.items():
        distance = node[0]
        if (distance == 0):
            distance = -1
        if (key != s):
            distances.append(distance)
    return distances

def validate_completion(nodes, q, edge_start, edge_end):
    if (nodes[edge_end][1] == False):
        nodes[edge_end][0] = 6 + nodes[edge_start][0]
        
        if (nodes[edge_start][1] == True):
            nodes[edge_end][1] = True

        q.put(edge_end)
    
def bfs(n, m, edges, s):
    nodes = {key: [0, False] for key in range(1, n + 1)}

    q = queue.Queue()
    q.put(s)
    nodes[s][1] = True
        
    while not q.empty():
        start = q.get()
        adjacentEdges = list(filter(lambda e: start in e, edges))
            
        for e in adjacentEdges:
            edge_start = e[0]
            edge_end = e[1]
            
            validate_completion(nodes, q, edge_start, edge_end)
            validate_completion(nodes, q, edge_end, edge_start)

    distances = transform_object(nodes, s)
    return distances            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
