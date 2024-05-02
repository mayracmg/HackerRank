def minimumDistances(a):
    min_distance = -1
    distances = {}

    i = 0
    for e in a:
        try:
            distance = i - distances[e]
            if min_distance == -1 or distance < min_distance:
                min_distance = distance
        except:
            distances[e] = i
        i = i + 1
    return min_distance
