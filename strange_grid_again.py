def strangeGrid(r, c):
    row = r - 1
    column = c - 1
    
    number =  ((row // 2) * 10) + (2 * column) + (row % 2)
    
    return number
