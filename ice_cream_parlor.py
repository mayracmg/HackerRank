def icecreamParlor(m, arr):
    total = 0
    prices = []
    n = len(arr)
    for i in range(n):
        p1 = arr[i]
        for j in range(i + 1, n):
            p2 = arr[j]
            
            if p1 + p2 >= total and p1 + p2 <= m:
                total = p1 + p2
                prices = [i + 1, j + 1]
    
    return prices
