def absolutePermutation(n, k):
    pos = []

    if k == 0 or (n / k) % 2 == 0:
        sign = 1
        for i in range(1, n + 1):
            pos.append(i + (k * sign))
            if k > 0 and i % k == 0:
                sign *= -1
    else:
        pos = [-1]

    return pos
