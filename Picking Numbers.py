def pickingNumbers(a):
    weights = {0:0}
    max_weight = 0
    prev_item = 0
        
    for item in a:
        try:
            weights[item] = weights[item] + 1
        except:
            weights[item] = 1
    
    for current_item in sorted(weights.keys()):
        current_weight = weights[current_item]
        if current_item - prev_item == 1:
            current_weight += weights[prev_item]
        
        max_weight = max(max_weight, current_weight)
        
        prev_item = current_item
    
    return max_weight
