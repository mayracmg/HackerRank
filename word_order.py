# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

n = int(input())
words = OrderedDict()

for i in range(n):
    w = input()
    try:
        words[w] += 1
    except:
        words[w] = 1
        
print(len(words))

for key, value in words.items():
    print(value, end=" ")
