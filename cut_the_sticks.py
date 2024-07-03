def cutTheSticks(arr):
    arr.sort()
    n = len(arr)
    r = [n]
        
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            r.append(n - i)
            
    return r
