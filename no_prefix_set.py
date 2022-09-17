import math
import os
import random
import re
import sys
import bisect

def noPrefix(words):
    prefixes = []
    
    for word in words:
        try:
            finded_index = bisect.bisect_left(prefixes, word)
            
            for i in range(finded_index - 1, finded_index + 1):
                temp_word = prefixes[i]
                
                if (word.startswith(temp_word) or temp_word.startswith(word) or word == temp_word):
                    print('BAD SET')
                    print(word)
                    return
        except:
            pass
        
        bisect.insort_left(prefixes, word)
    
    print('GOOD SET')

if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
