def encryption(s):
    l = len(s)
    rows = math.floor(math.sqrt(l))
    cols = math.ceil(math.sqrt(l))
    new_s = ''
    rows = rows + 1 if rows * cols < l else rows
    
    for i in range(cols):
        for j in range(rows):
            k = i + j * cols
            if k < l:
                new_s += s[k]
            
        new_s += ' '
   
    return new_s
